# supabase-secrets-generator

A small utility to generate secrets and signed JWTs for Supabase.

```shell
JWT_KEY=$(supabase-secrets-generator key);
ANON_JWT=$(supabase-secrets-generator anon-role "$JWT_KEY");
SERVICE_JWT=$(supabase-secrets-generator service-role "$JWT_KEY");
```