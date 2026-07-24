import { useEffect, useRef } from 'react'

// Lightweight canvas "data node" background: dots drift and connect with
// thin lines when close, echoing a network / data-graph motif relevant
// to a data & AI portfolio, without pulling in a heavy particles library.
export default function ParticlesBackground() {
  const canvasRef = useRef(null)

  useEffect(() => {
    const canvas = canvasRef.current
    const ctx = canvas.getContext('2d')
    let width, height, particles, animationId
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches

    const colors = ['#3B82F6', '#8B5CF6', '#06B6D4']

    function resize() {
      width = canvas.width = canvas.offsetWidth
      height = canvas.height = canvas.offsetHeight
    }

    function init() {
      resize()
      const count = Math.min(60, Math.floor((width * height) / 22000))
      particles = Array.from({ length: count }, () => ({
        x: Math.random() * width,
        y: Math.random() * height,
        vx: (Math.random() - 0.5) * 0.25,
        vy: (Math.random() - 0.5) * 0.25,
        r: Math.random() * 1.6 + 0.6,
        color: colors[Math.floor(Math.random() * colors.length)],
      }))
    }

    function draw() {
      ctx.clearRect(0, 0, width, height)
      particles.forEach((p) => {
        p.x += p.vx
        p.y += p.vy
        if (p.x < 0 || p.x > width) p.vx *= -1
        if (p.y < 0 || p.y > height) p.vy *= -1
      })

      for (let i = 0; i < particles.length; i++) {
        for (let j = i + 1; j < particles.length; j++) {
          const a = particles[i]
          const b = particles[j]
          const d = Math.hypot(a.x - b.x, a.y - b.y)
          if (d < 130) {
            ctx.strokeStyle = `rgba(139,92,246,${0.12 * (1 - d / 130)})`
            ctx.lineWidth = 1
            ctx.beginPath()
            ctx.moveTo(a.x, a.y)
            ctx.lineTo(b.x, b.y)
            ctx.stroke()
          }
        }
      }

      particles.forEach((p) => {
        ctx.beginPath()
        ctx.fillStyle = p.color
        ctx.globalAlpha = 0.7
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2)
        ctx.fill()
        ctx.globalAlpha = 1
      })

      animationId = requestAnimationFrame(draw)
    }

    init()
    if (!prefersReducedMotion) {
      draw()
    } else {
      // Draw a single static frame for reduced-motion users
      draw()
      cancelAnimationFrame(animationId)
    }

    const handleResize = () => init()
    window.addEventListener('resize', handleResize)
    return () => {
      cancelAnimationFrame(animationId)
      window.removeEventListener('resize', handleResize)
    }
  }, [])

  return (
    <canvas
      ref={canvasRef}
      className="pointer-events-none absolute inset-0 h-full w-full opacity-70"
      aria-hidden="true"
    />
  )
}
