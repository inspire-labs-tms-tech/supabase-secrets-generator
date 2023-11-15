# supabase-secrets-generator

A small utility to generate secrets and signed JWTs for Supabase (intended to be used in shell scripts automating the deployment of self-hosted instances of Supabase).

## Script Example

Write the JWT Key and JWTs to environment variables (for use in later processing in your scripts, such as writing to a `.env` file).

```shell
JWT_KEY=$(supabase-secrets-generator key);
ANON_JWT=$(supabase-secrets-generator anon-role "$JWT_KEY");
SERVICE_JWT=$(supabase-secrets-generator service-role "$JWT_KEY");
```
