# Subprojects

This is the parent area for independent learning builds. Do not create a project folder until a session establishes a clear purpose and boundary.

Suggested layout for a future project:

```text
projects/<purposeful-name>/
├── README.md          # problem, users, architecture, commands, cost notes
├── pyproject.toml     # or another project-owned dependency manifest
├── src/
├── tests/
├── infra/             # project-owned Terraform and teardown notes
├── docs/              # decisions and operational guidance
└── .env.example       # names only; never credentials
```

Conventions:

- A project owns its dependencies, lock files, infrastructure, and commands.
- Persistent resources and destructive teardown steps are named explicitly.
- Record infrastructure, licence, and expected maintenance costs.
- Prefer synthetic or appropriately licensed data; document provenance and sensitivity.
- Keep secrets out of the repository and generated data out of version control.
- Move something into a shared area only after at least two projects need the same stable asset.

