// tool definitions for MCP exposure

export const TOOLS = [
  {
    name: "search",
    description: "search agent memory and knowledge base",
    inputSchema: {
      type: "object",
      properties: {
        query: { type: "string", description: "search query" },
        limit: { type: "number", description: "max results", default: 10 },
      },
      required: ["query"],
    },
  },
  {
    name: "execute",
    description: "execute a tool in the agent runtime",
    inputSchema: {
      type: "object",
      properties: {
        tool: { type: "string" },
        args: { type: "object" },
      },
      required: ["tool"],
    },
  },
  {
    name: "plan",
    description: "generate an execution plan for a task",
    inputSchema: {
      type: "object",
      properties: {
        task: { type: "string" },
        constraints: { type: "array", items: { type: "string" } },
      },
      required: ["task"],
    },
  },
  {
    name: "memory",
    description: "read/write agent memory",
    inputSchema: {
      type: "object",
      properties: {
        action: { type: "string", enum: ["get", "set", "search"] },
        key: { type: "string" },
        value: {},
      },
      required: ["action"],
    },
  },
];
