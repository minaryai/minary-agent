// MCP server — work in progress
// Protocol: https://spec.modelcontextprotocol.io

export class MCPServer {
  constructor(opts = {}) {
    this.tools = new Map();
    this.port = opts.port || 3100;
  }

  registerTool(name, schema, handler) {
    this.tools.set(name, { schema, handler });
  }

  async start() {
    // TODO: implement MCP transport (stdio + HTTP)
    console.log(`mcp server listening on ${this.port}`);
  }
}
