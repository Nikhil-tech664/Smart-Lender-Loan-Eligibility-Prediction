# Frontend UI/UX and Interactive Implementation

The user interface of **SmartLender AI** is implemented as a modern, responsive Single Page Application (SPA).

## 1. UI/UX Style and Styling Tokens
- **Theme:** Dark navy banking theme (`#0b1329`) utilizing background blur glassmorphism properties (`backdrop-filter: blur(20px)`), ambient glowing blobs, and glowing title underlines.
- **Micro-Animations:** Form buttons feature shimmer animations (`.btn-shimmer`), and badges pulse dynamically to indicate active states.
- **Theme Toggle:** Supports theme toggling between dark navy and light layouts via `localStorage`.

---

## 2. Interactive Client JavaScript Logic (`main.js`)
* **Dual Slider Synchronization:** Synchronizes numerical inputs with responsive range sliders for a more user-friendly interface.
* **Stepped Loader Engine:** Displays a 6-stage loading indicator (e.g. "Checking Credit History...", "Running ML Model...") to manage perceived latency during predictions.
* **Canvas Donut Gauge:** Renders a responsive semi-circular gauge using Chart.js to visualize approval probability, and launches `canvas-confetti` celebrations upon approval.
* **Local History Manager:** Automatically saves up to 20 past results in the browser's local memory. Features real-time search, status filtering (`Approved` vs `Rejected`), and sorting options.
* **Data Export Utilities:** Exports results locally to PDF (Print layout), structured CSV files, or raw JSON payloads.
