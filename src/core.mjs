// core agent loop logic
export class AgentCore {
  constructor(opts = {}) {
    this.model = opts.model || 'claude-4.7-sonnet';
    this.maxIterations = opts.maxIterations || 8;
    this.tools = new Map();
  }

  registerTool(name, handler, schema) {
    this.tools.set(name, { handler, schema });
  }

  async step(messages) {
    // placeholder: call LLM, parse response, execute tools
    return { type: 'end', content: 'scaffold — wire up LLM client' };
  }
}
