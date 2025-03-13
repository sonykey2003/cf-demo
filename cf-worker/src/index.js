export default {
    async fetch(request, env, ctx) {
      const url = new URL(request.url);
  
      if (url.pathname === '/secure') {
        const country = request.headers.get('cf-ipcountry') || 'SG';
        const time = new Date().toISOString();
        const email = request.headers.get('cf-access-authenticated-user-email') || 'user@example.com';
  
        let flagUrl;
        if (country.toLowerCase() === 'sg') {
          flagUrl = 'https://theantechs.com/Flag_of_Singapore.svg.png';
        } else if (country.toLowerCase() === 'th') {
          flagUrl = 'https://theantechs.com/Flag_of_Thailand.svg.png';
        } else {
          flagUrl = '';
        }
  
        const html = `
          <html>
            <body>
              <h1>Authenticated User Information</h1>
              <p>Email: ${request.headers.get('cf-access-authenticated-user-email') || 'Unknown'}</p>
              <p>User IP Country: ${country}</p>
              <p>Authenticated at: ${time}</p>
              ${flagUrl ? `<p>Country flag: <img src="${flagUrl}" alt="${country} flag" style="width:50px;height:auto;"></p>` : ''}
            </body>
          </html>
        `;
  
        return new Response(html, {
          headers: { 'Content-Type': 'text/html' },
        });
      }
  
      return new Response('Not Found', { status: 404 });
    },
  };
  