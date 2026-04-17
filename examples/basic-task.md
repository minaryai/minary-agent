# basic task example

```bash
node src/cli.mjs "read the file at ./README.md and summarize it"
```

expected behavior:
1. agent plans: read file -> summarize
2. calls file_read tool
3. generates summary
4. returns result
