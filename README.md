# Next.js MVP Template

A production-ready Next.js template with TypeScript, Tailwind CSS, SQLite + Prisma, and persona-based development workflow.

## 🚀 Quick Start

```bash
# Install dependencies
npm install

# Set up database
npx prisma generate
npx prisma migrate dev

# Start development server
npm run dev
```

Open [http://localhost:3003](http://localhost:3003) to see your app.

## 📊 Code Line Counter

A Python script is included to analyze your codebase:

```bash
# Basic usage - analyze src directory
python3 count_lines.py

# Show file lists
python3 count_lines.py --show-files

# Analyze different directory
python3 count_lines.py --path .

# Save JSON report
python3 count_lines.py --json

# Full analysis with JSON output
python3 count_lines.py --show-files --json --json-output my_report.json
```

The script provides:
- Line counts by programming language
- Code vs blank line ratios
- File distribution across languages
- Visual representation of language usage
- Optional JSON export for further analysis

## 🏗️ Project Structure

```
├── src/                    # Source code
│   ├── app/               # Next.js App Router
│   ├── components/        # React components
│   ├── lib/              # Utilities
│   └── styles/           # CSS files
├── prisma/               # Database schema
├── CLAUDE/               # AI context files
│   ├── OUTLINE.md       # Project specifications
│   ├── WHITEBOARD.md    # Progress tracking
│   └── LEGACY/          # Old codebase (optional)
└── .claude/             # Persona configurations
```

## 🛠️ Tech Stack

- **Frontend**: Next.js 14 + TypeScript
- **Styling**: Tailwind CSS
- **Database**: SQLite + Prisma ORM
- **Development**: Persona-based workflow

## 📝 Development Workflow

This template uses a persona-based development approach with three specialized agents:
- **Designer**: UI/UX design and mockups
- **Frontend**: React/Next.js implementation
- **Backend**: API and database development

Check `.claude/agents/` for persona configurations and `CLAUDE.md` for the complete workflow documentation.

## 📦 Available Scripts

```bash
npm run dev          # Start development server (port 3003)
npm run build        # Build for production
npm run start        # Start production server
npm run lint         # Run ESLint
npm run typecheck    # Run TypeScript compiler check
```

## 🔧 Environment Variables

Create a `.env` file in the root:

```env
DATABASE_URL="file:./dev.db"
```

## 📄 License

MIT