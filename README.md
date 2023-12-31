# supabase-secrets-generator

A small utility to generate secrets and signed JWTs for Supabase (intended to be used in shell scripts automating the deployment of self-hosted instances of Supabase).

## Install

1. Download the version matching your system:
- MacOS: `wget -O supabase-secrets-generator.tar.gz https://github.com/inspire-labs-tms-tech/supabase-secrets-generator/releases/download/latest/macos.tar.gz`
- Ubuntu: `wget -O supabase-secrets-generator.tar.gz https://github.com/inspire-labs-tms-tech/supabase-secrets-generator/releases/download/latest/ubuntu.tar.gz`

2. Extract the utility: `tar -xf supabase-secrets-generator.tar.gz`
3. Make `supabase-secrets-generator` executable: `chmod a+x supabase-secrets-generator`
4. (Optional) Make `supabase-secrets-generator` visible in your path: `sudo mv supabase-secrets-generator /usr/local/bin/supabase-secrets-generator`

## Script Example

Write the JWT Key and JWTs to environment variables (for use in later processing in your scripts, such as writing to a `.env` file).

```shell
JWT_KEY=$(supabase-secrets-generator key);
ANON_JWT=$(supabase-secrets-generator anon-role "$JWT_KEY");
SERVICE_JWT=$(supabase-secrets-generator service-role "$JWT_KEY");
```
