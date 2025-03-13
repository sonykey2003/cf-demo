# CloudFlare Secured Demo Webapp

This project consists of:

- A **main Flask app** that handles role-based redirects. (SAML)
- Two **role-specific Flask apps** (IT and HR pages).
- A **Cloudflare Worker** providing authenticated user information and country flags.
- Containerized using Docker Compose with Cloudflare Tunnel for secure public access.

## Prerequisites

- [Docker](https://www.docker.com/) and Docker Compose installed.
- Cloudflare account with Cloudflare Tunnel [configured](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/get-started/create-remote-tunnel/).

## Project Structure

```
.
├── main_app/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── page_app/
│   ├── Dockerfile
│   ├── pages.py
│   └── requirements.txt
├── cloudflared/
│   └── Dockerfile
├── cloudflare-worker/
│   ├── wrangler.toml
│   └── src/
│       └── index.js
└── docker-compose.yml
```

## Running the Application & CF Tunnel


```bash
export CLOUDFLARED_TOKEN="your-tunnel-token"
docker-compose up -d --build
```

- Main App at: `http://localhost:5500`
- IT page at `http://localhost:5600`
- HR page at `http://localhost:5700`
- CloudFlared Tunnel agent will proxy the app's traffic securely to CF servers.



## Cloudflare Worker

Your Cloudflare Worker serves an authenticated user page at `/secure`, showing:

- User email
- IP-based country
- Authentication timestamp
- Country-specific flags

Flags are fetched from R2 Bucket `demo`.

Deploy your Worker:

```bash
npm install -g wrangler
wrangler deploy
```

Access via:

- Secure info: `https://tunnel.theantechs.com/secure`
- Flags: automatically displayed based on user's IP.

