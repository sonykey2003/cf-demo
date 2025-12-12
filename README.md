# CloudFlare Secured Demo Webapp

This project consists of:

- A **main Flask app** that handles role-based redirects. (SAML)
- Two **role-specific Flask apps** (IT and HR pages).
- A **Cloudflare Worker** providing authenticated user information and country flags.
- Containerized using Docker Compose with Cloudflare Tunnel for secure public access.

## Prerequisites

- [Docker](https://www.docker.com/) and Docker Compose installed.
- A free Cloudflare account.

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

# Run The Application Locally
* In Main/main.py, uncomment line 12 and comment out line 13:
```py
return redirect(f"http://{localhost}:5600", code=302)
#return redirect(f"http://it.{domain}", code=302)
```
* Do the same on line 18,19:
```py
return redirect(f"http://{localhost}:5700", code=302)
#return redirect(f"http://hr.{domain}", code=302)
```
* Run the app:
```bash
docker-compose up -d --build
```

- Main App at: `http://localhost:5500`
- IT page at `http://localhost:5600`
- HR page at `http://localhost:5700`
## Run the Application On Internet

* Reverse the changes in Main/main.py.
* Run the app:

```bash
export CLOUDFLARED_TOKEN="your-tunnel-token"
docker-compose up -d --build
```

- Setup Cloudflare Tunnel [configured](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/get-started/create-remote-tunnel/).
  * Make sure using the container names when publishing the application:<img src="https://github.com/user-attachments/assets/f20e99ec-32cd-4ac8-a882-a861958310eb"  width=80% height=80%>

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

