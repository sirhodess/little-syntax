import { useState } from "react";
import "./App.css";

type RunResponse = {
  output: string[];
  errors: string[];
  variables: Record<string, unknown>;
};

type Quest = {
  id: "name" | "lantern" | "coins";
  title: string;
  description: string;
  guideIcon: string;
  guideName: string;
  guideSpeech: string;
  challengeIcon: string;
  challengeName: string;
  challengeSpeech: string;
  starterCode: string;
  tileIndex: number;
};

const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL ?? "http://127.0.0.1:8000";

const quests: Quest[] = [
  {
    id: "name",
    title: "Say Your Name",
    description:
      "The quest board is asleep. Create a name variable and say it aloud so the map knows who you are.",
    guideIcon: "🧙",
    guideName: "Map Magician",
    guideSpeech: "I cannot see you yet. Tell the board your name.",
    challengeIcon: "✨",
    challengeName: "Name Rune",
    challengeSpeech: "Say your name, and the first rune will wake.",
    starterCode: `let name = "Milo"
say name`,
    tileIndex: 1,
  },
  {
    id: "lantern",
    title: "Light the Lantern",
    description:
      "The map can see you now, but the path is dark. Use a repeat loop to make the lantern glow.",
    guideIcon: "🧙",
    guideName: "Map Magician",
    guideSpeech: "I can see you now, but I cannot see the path. Light the lantern.",
    challengeIcon: "🏮",
    challengeName: "Sleeping Lantern",
    challengeSpeech: "Repeat Glow three times to light the way.",
    starterCode: `repeat 3 {
  say "Glow!"
}`,
    tileIndex: 2,
  },
  {
    id: "coins",
    title: "Pay the Bridge Troll",
    description:
      "The lantern reveals a bridge, but a troll blocks the gate. Check whether you have enough coins.",
    guideIcon: "🧌",
    guideName: "Gate Troll",
    guideSpeech: "Bring 5 coins, and I will open the gate.",
    challengeIcon: "🚪",
    challengeName: "Locked Gate",
    challengeSpeech: "Use an if statement to decide whether the gate opens.",
    starterCode: `let coins = 5

if coins >= 5 {
  say "The gate opens!"
} else {
  say "You need more coins."
}`,
    tileIndex: 4,
  },
];

const finalQuest = {
  title: "Gate Opened",
  description:
    "The troll steps aside, the gate creaks open, and the little kingdom road continues.",
  guideIcon: "🏰",
  guideName: "Kingdom Gate",
  guideSpeech: "Quest complete! The path ahead is open.",
  challengeIcon: "✨",
  challengeName: "Bright Path",
  challengeSpeech: "You used variables, output, loops, and conditionals.",
};

function checkQuestPassed(quest: Quest, result: RunResponse) {
  if (result.errors.length > 0) {
    return false;
  }

  if (quest.id === "name") {
    const name = result.variables.name;

    return (
      typeof name === "string" &&
      name.trim().length > 0 &&
      result.output.includes(name)
    );
  }

  if (quest.id === "lantern") {
    const glowCount = result.output.filter((line) => line === "Glow!").length;
    return glowCount >= 3;
  }

  if (quest.id === "coins") {
    return result.output.includes("The gate opens!");
  }

  return false;
}

function App() {
  const [activeQuestIndex, setActiveQuestIndex] = useState(0);
  const [completedQuestIds, setCompletedQuestIds] = useState<string[]>([]);
  const [source, setSource] = useState(quests[0].starterCode);
  const [result, setResult] = useState<RunResponse | null>(null);
  const [isRunning, setIsRunning] = useState(false);
  const [isConsoleOpen, setIsConsoleOpen] = useState(false);

  const currentQuest = quests[activeQuestIndex];
  const allQuestsComplete = completedQuestIds.length === quests.length;

  const visibleQuest = allQuestsComplete
    ? finalQuest
    : {
        title: currentQuest.title,
        description: currentQuest.description,
        guideIcon: currentQuest.guideIcon,
        guideName: currentQuest.guideName,
        guideSpeech: currentQuest.guideSpeech,
        challengeIcon: currentQuest.challengeIcon,
        challengeName: currentQuest.challengeName,
        challengeSpeech: currentQuest.challengeSpeech,
      };

  const currentTile = allQuestsComplete ? 5 : currentQuest.tileIndex;

  async function runCode() {
    setIsRunning(true);

    try {
      const response = await fetch(`${API_BASE_URL}/run`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ source }),
      });

      const data = (await response.json()) as RunResponse;
      const passed = checkQuestPassed(currentQuest, data);

      setResult(data);

      if (passed) {
        setCompletedQuestIds((previousIds) =>
          previousIds.includes(currentQuest.id)
            ? previousIds
            : [...previousIds, currentQuest.id],
        );

        if (activeQuestIndex < quests.length - 1) {
          const nextQuestIndex = activeQuestIndex + 1;
          setActiveQuestIndex(nextQuestIndex);
          setSource(quests[nextQuestIndex].starterCode);
        }
      }

      setIsConsoleOpen(false);
    } catch {
      setResult({
        output: [],
        errors: [
          "Could not reach the Little Syntax API. Make sure the backend is running.",
        ],
        variables: {},
      });
    } finally {
      setIsRunning(false);
    }
  }

  function resetQuestLine() {
    setActiveQuestIndex(0);
    setCompletedQuestIds([]);
    setSource(quests[0].starterCode);
    setResult(null);
    setIsConsoleOpen(false);
  }

  return (
    <main className="board-page">
      <div className="map-layer" aria-hidden="true">
        <span className="cloud cloud-one">☁️</span>
        <span className="cloud cloud-two">☁️</span>
        <span className="map-sparkle sparkle-one">✦</span>
        <span className="map-sparkle sparkle-two">✧</span>
        <span className="map-sparkle sparkle-three">✦</span>
        <span className="forest forest-one">🌲</span>
        <span className="forest forest-two">��</span>
        <span className="castle-marker">��</span>
      </div>

      <header className="top-bar">
        <div>
          <p className="eyebrow">Little Syntax</p>
          <h1>A tiny coding quest board for beginner programmers.</h1>
        </div>

        <button
          className="console-toggle"
          onClick={() => setIsConsoleOpen(true)}
        >
          Open Code Panel
        </button>
      </header>

      <section className="map-stage" aria-label="Little Syntax quest board">
        <article className="quest-scroll">
          <p className="section-label">
            {allQuestsComplete
              ? "Quest Complete"
              : `Quest ${activeQuestIndex + 1} of ${quests.length}`}
          </p>
          <h2>{visibleQuest.title}</h2>
          <p>{visibleQuest.description}</p>
        </article>

        <article className="board-character dragon-card">
          <span className="character-token" aria-hidden="true">
            {visibleQuest.guideIcon}
          </span>
          <div>
            <h3>{visibleQuest.guideName}</h3>
            <p>{visibleQuest.guideSpeech}</p>
          </div>
        </article>

        <div className="map-route" aria-label="Quest progress path">
          {[1, 2, 3, 4, 5].map((tile) => (
            <div
              key={tile}
              className={`path-tile ${tile <= currentTile ? "active" : ""}`}
            >
              {tile === 1 && "🧙"}
              {tile === 2 && "🏮"}
              {tile === 3 && "🌉"}
              {tile === 4 && "🧌"}
              {tile === 5 && "🏰"}
            </div>
          ))}
        </div>

        <article className="board-character troll-card">
          <span className="character-token" aria-hidden="true">
            {visibleQuest.challengeIcon}
          </span>
          <div>
            <h3>{visibleQuest.challengeName}</h3>
            <p>{visibleQuest.challengeSpeech}</p>
          </div>
        </article>

        <article className="status-card">
          <span>Quest Status</span>
          <strong>
            {allQuestsComplete ? "All quests complete!" : visibleQuest.title}
          </strong>

          <button onClick={() => setIsConsoleOpen(true)}>
            {allQuestsComplete ? "View Code Panel" : "Write Code for This Quest"}
          </button>

          {allQuestsComplete && (
            <button className="secondary-action" onClick={resetQuestLine}>
              Restart Quest Line
            </button>
          )}
        </article>
      </section>

      {isConsoleOpen && (
        <div
          className="drawer-backdrop"
          onClick={() => setIsConsoleOpen(false)}
          aria-hidden="true"
        />
      )}

      <aside
        className={`code-drawer ${isConsoleOpen ? "code-drawer-open" : ""}`}
        aria-label="Quest console"
        aria-hidden={!isConsoleOpen}
      >
        <div className="drawer-header">
          <div>
            <p className="section-label">Quest Console</p>
            <h2>Your Code</h2>
            <p className="drawer-quest-title">{currentQuest.title}</p>
          </div>

          <button
            className="close-button"
            onClick={() => setIsConsoleOpen(false)}
            aria-label="Close code panel"
          >
            ×
          </button>
        </div>

        <textarea
          value={source}
          onChange={(event) => setSource(event.target.value)}
          spellCheck={false}
          aria-label="Little Syntax code editor"
        />

        <button className="run-button" onClick={runCode} disabled={isRunning}>
          {isRunning ? "Running..." : "Run Quest"}
        </button>

        <div className="example-row">
          <button onClick={() => setSource(currentQuest.starterCode)}>
            Use Starter Code
          </button>
          <button onClick={resetQuestLine}>Reset Quest Line</button>
        </div>

        <section className="result-box">
          <h3>Quest Result</h3>

          {result === null && (
            <p className="muted">Run your code to see what happens.</p>
          )}

          {result?.output.map((line, index) => (
            <p key={`${line}-${index}`} className="output-line">
              ✨ {line}
            </p>
          ))}

          {result?.errors.map((error, index) => (
            <p key={`${error}-${index}`} className="error-line">
              ⚠ {error}
            </p>
          ))}
        </section>

        <section className="result-box">
          <h3>Collected Values</h3>
          <pre>
            {result ? JSON.stringify(result.variables, null, 2) : "No variables yet."}
          </pre>
        </section>
      </aside>
    </main>
  );
}

export default App;
