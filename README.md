# Hedron

This is a standalone Next.js app. The old Docker/MongoDB startup path has been removed, and the former OpenAI/Mongo route implementations are preserved under `deprecated-ai/` for future rewiring.

## Development

```bash
npm install
npm run dev
```

Open http://localhost:3000.

## Production

```bash
npm run build
npm run start
```

The live `/api/gpt` and `/api/msg` routes currently return static deprecated responses, so the app no longer needs MongoDB or OpenAI credentials to start.
