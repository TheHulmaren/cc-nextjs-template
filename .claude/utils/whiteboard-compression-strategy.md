# WHITEBOARD.md Compression Strategies

## 1. **Archive Completed Sections**
Create `CLAUDE/ARCHIVED/` folder with dated files:
- `WHITEBOARD-2025-01-13.md` for completed sprints
- Do not create dedicated archived file for each persona; keep it in one-piece.
- Keep only active/pending tasks in main WHITEBOARD.md
- ⚠️ **WARNING:** Each archived file should NOT exceed 200 lines to maintain readability
- You can make it reasonably dense. Preserve details within the length limit.

## 2. **Task Summarization Pattern**
Replace verbose task descriptions with concise summaries:
```markdown
<!-- Instead of: -->
TASKS:
- Implemented user authentication with JWT tokens, added login/logout endpoints, 
  created middleware for route protection, integrated with SQLite database...

<!-- Use: -->
TASKS:
- ✅ Auth system (JWT, login/logout, middleware)
```

## 3. **Use Reference Links**
For detailed implementations, reference code locations:
```markdown
TASKS:
- ✅ Post CRUD APIs → /api/posts/[id]/route.ts
- ✅ Auth middleware → /middleware/auth.ts
```

**Recommendation:** Use strategy #1 (Archive) + #3 (References). Archive completed work weekly, keep WHITEBOARD focused on current sprint only.