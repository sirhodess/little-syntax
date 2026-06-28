import { useEffect, useRef } from "react";
import "./DragonIntro.css";

type DragonIntroProps = {
  onDone: () => void;
};

function drawDragon(
  ctx: CanvasRenderingContext2D,
  x: number,
  y: number,
  scale: number,
  wingFlap: number,
  firePower: number,
) {
  ctx.save();
  ctx.translate(x, y);
  ctx.scale(scale, scale);

  const purple = "#6f55a6";
  const darkPurple = "#4d3b78";
  const gold = "#f3c96b";

  // Tail
  ctx.strokeStyle = purple;
  ctx.lineWidth = 18;
  ctx.lineCap = "round";
  ctx.beginPath();
  ctx.moveTo(-42, 18);
  ctx.bezierCurveTo(-88, 28, -124, 18, -156, -16);
  ctx.stroke();

  // Back wing
  ctx.save();
  ctx.translate(-10, -12);
  ctx.rotate(-0.25 + wingFlap * 0.25);
  ctx.fillStyle = darkPurple;
  ctx.beginPath();
  ctx.moveTo(0, 0);
  ctx.quadraticCurveTo(-72, -120, 16, -88);
  ctx.quadraticCurveTo(58, -48, 18, 4);
  ctx.closePath();
  ctx.fill();
  ctx.restore();

  // Body
  ctx.fillStyle = purple;
  ctx.beginPath();
  ctx.ellipse(0, 12, 62, 38, 0, 0, Math.PI * 2);
  ctx.fill();

  // Belly
  ctx.fillStyle = "#a997d7";
  ctx.beginPath();
  ctx.ellipse(12, 20, 30, 18, 0, 0, Math.PI * 2);
  ctx.fill();

  // Neck
  ctx.strokeStyle = purple;
  ctx.lineWidth = 18;
  ctx.beginPath();
  ctx.moveTo(44, 0);
  ctx.quadraticCurveTo(70, -28, 92, -12);
  ctx.stroke();

  // Head
  ctx.fillStyle = purple;
  ctx.beginPath();
  ctx.ellipse(106, -10, 32, 23, 0.12, 0, Math.PI * 2);
  ctx.fill();

  // Snout
  ctx.beginPath();
  ctx.ellipse(132, -5, 20, 13, 0.1, 0, Math.PI * 2);
  ctx.fill();

  // Horn
  ctx.fillStyle = gold;
  ctx.beginPath();
  ctx.moveTo(96, -30);
  ctx.lineTo(105, -52);
  ctx.lineTo(114, -28);
  ctx.closePath();
  ctx.fill();

  // Eye
  ctx.fillStyle = "#fffaf1";
  ctx.beginPath();
  ctx.arc(112, -15, 5, 0, Math.PI * 2);
  ctx.fill();

  ctx.fillStyle = "#251b35";
  ctx.beginPath();
  ctx.arc(113, -15, 2.3, 0, Math.PI * 2);
  ctx.fill();

  // Nostril
  ctx.beginPath();
  ctx.arc(137, -2, 2.4, 0, Math.PI * 2);
  ctx.fill();

  // Front wing
  ctx.save();
  ctx.translate(12, -18);
  ctx.rotate(0.1 + wingFlap * 0.35);
  ctx.fillStyle = purple;
  ctx.beginPath();
  ctx.moveTo(0, 0);
  ctx.quadraticCurveTo(80, -120, 126, -16);
  ctx.quadraticCurveTo(62, -8, 10, 10);
  ctx.closePath();
  ctx.fill();
  ctx.restore();

  // Legs
  ctx.strokeStyle = purple;
  ctx.lineWidth = 10;
  ctx.lineCap = "round";
  ctx.beginPath();
  ctx.moveTo(-18, 38);
  ctx.lineTo(-28, 60);
  ctx.moveTo(22, 38);
  ctx.lineTo(14, 62);
  ctx.stroke();

  // Spikes
  ctx.fillStyle = gold;
  [-30, -8, 14, 36].forEach((sx, index) => {
    const sy = index % 2 === 0 ? -24 : -31;
    ctx.beginPath();
    ctx.moveTo(sx - 6, sy + 8);
    ctx.lineTo(sx, sy - 10);
    ctx.lineTo(sx + 6, sy + 8);
    ctx.closePath();
    ctx.fill();
  });

  // Fire
  if (firePower > 0) {
    const length = 180 * firePower;
    const gradient = ctx.createLinearGradient(148, -4, 148 + length, -4);
    gradient.addColorStop(0, "rgba(255, 245, 186, 0.95)");
    gradient.addColorStop(0.35, "rgba(255, 184, 74, 0.95)");
    gradient.addColorStop(0.7, "rgba(255, 103, 55, 0.9)");
    gradient.addColorStop(1, "rgba(255, 103, 55, 0)");

    ctx.fillStyle = gradient;
    ctx.beginPath();
    ctx.moveTo(148, -18);
    ctx.quadraticCurveTo(148 + length * 0.62, -58, 148 + length, -4);
    ctx.quadraticCurveTo(148 + length * 0.62, 46, 148, 12);
    ctx.closePath();
    ctx.fill();
  }

  ctx.restore();
}

export default function DragonIntro({ onDone }: DragonIntroProps) {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);

  useEffect(() => {
    const prefersReducedMotion = window.matchMedia(
      "(prefers-reduced-motion: reduce)",
    ).matches;

    if (prefersReducedMotion) {
      onDone();
      return;
    }

    const canvas = canvasRef.current;
    const ctx = canvas?.getContext("2d");

    if (!canvas || !ctx) {
      onDone();
      return;
    }

    let animationFrame = 0;
    let startTime = 0;
    const duration = 2800;

    function resize() {
      const dpr = window.devicePixelRatio || 1;
      canvas.width = window.innerWidth * dpr;
      canvas.height = window.innerHeight * dpr;
      canvas.style.width = `${window.innerWidth}px`;
      canvas.style.height = `${window.innerHeight}px`;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }

    function render(time: number) {
      if (!startTime) startTime = time;

      const elapsed = time - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const fade = progress < 0.82 ? 1 : 1 - (progress - 0.82) / 0.18;

      const width = window.innerWidth;
      const height = window.innerHeight;

      ctx.clearRect(0, 0, width, height);

      const background = ctx.createLinearGradient(0, 0, 0, height);
      background.addColorStop(0, `rgba(255, 249, 239, ${0.98 * fade})`);
      background.addColorStop(0.45, `rgba(246, 238, 255, ${0.95 * fade})`);
      background.addColorStop(1, `rgba(244, 230, 199, ${0.92 * fade})`);

      ctx.fillStyle = background;
      ctx.fillRect(0, 0, width, height);

      const easeOut = 1 - Math.pow(1 - Math.min(progress / 0.72, 1), 3);
      const dragonX = -220 + easeOut * (width * 0.7);
      const dragonY = height * 0.38 + Math.sin(time * 0.004) * 12;
      const wingFlap = Math.sin(time * 0.022);
      const firePower =
        progress > 0.3 && progress < 0.62
          ? Math.sin(((progress - 0.3) / 0.32) * Math.PI)
          : 0;

      ctx.globalAlpha = fade;
      drawDragon(ctx, dragonX, dragonY, 1.2, wingFlap, firePower);

      ctx.fillStyle = "rgba(73, 52, 111, 0.9)";
      ctx.font = "900 18px Inter, system-ui, sans-serif";
      ctx.textAlign = "center";
      ctx.fillText("Waking the quest board...", width / 2, height * 0.82);
      ctx.globalAlpha = 1;

      if (progress < 1) {
        animationFrame = window.requestAnimationFrame(render);
      } else {
        onDone();
      }
    }

    resize();
    window.addEventListener("resize", resize);
    animationFrame = window.requestAnimationFrame(render);

    return () => {
      window.cancelAnimationFrame(animationFrame);
      window.removeEventListener("resize", resize);
    };
  }, [onDone]);

  return (
    <div className="dragon-intro-overlay" aria-hidden="true">
      <canvas ref={canvasRef} className="dragon-intro-canvas" />
    </div>
  );
}
