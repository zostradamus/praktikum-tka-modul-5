# TKA Modul 5 — Cloudsim dan Load Balancing

**Question Source:** [Cloud Computing Practicum Module 5](https://docs.google.com/document/d/1DZ1yEOJUnh68muG9g-kqsf85Um7wxdD5A-fxH-7b6-E/edit?tab=t.0)

## Group B08 Members

| No | Name | GitHub |
|----|------|--------|
| 1 | Adiwidya | [@Riverzn](https://github.com/Riverzn) |
| 2 | Prabaswara | [@zostradamus](https://github.com/zostradamus) |
| 3 | Zelig | [@zelebwr](https://github.com/zelebwr) |

## Question 1 — TokoKita Load Balancer
Sets up a load balancing system for TokoKita's e-commerce backend using NGINX with Weighted Round Robin algorithm, distributing traffic across 2 Flask backend servers:
- **Backend 1** — Server 1 - TokoKita (weight = 3)
- **Backend 2** — Server 2 - TokoKita (weight = 1)

### Services
| Service | Image | Port |
|---------|-------|------|
| backend1 | custom build (python:3.9-slim) | 5001 |
| backend2 | custom build (python:3.9-slim) | 5002 |
| nginx | custom build (nginx:alpine) | 80 |

### Project Structure
```
TokoKita/
├── backend1/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── backend2/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── nginx/
│   ├── Dockerfile
│   └── nginx.conf
└── docker-compose.yml
```

### API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Menampilkan identitas server dan hostname |
| `/products` | GET | Menampilkan daftar produk dalam format JSON |

### Key Configurations
- Load Balancer: **NGINX** dengan algoritma **Weighted Round Robin**
- Backend 1 weight: **3** (menerima 3x lebih banyak request)
- Backend 2 weight: **1**
- Traffic distribution pattern: **3:1** (3x Server 1, 1x Server 2)

### NGINX Upstream Configuration
```nginx
upstream app {
    server backend1:5000 weight=3;
    server backend2:5000 weight=1;
}
```

---

## How to Run
```bash
# Masuk ke folder TokoKita
cd TokoKita

# Build dan jalankan semua service
docker-compose up --build

# Verifikasi container berjalan
docker ps
```

### Access Points
| Service | URL |
|---------|-----|
| Load Balancer (NGINX) | http://localhost |
| Product List | http://localhost/products |
| Backend 1 (direct) | http://localhost:5001 |
| Backend 2 (direct) | http://localhost:5002 |

### Verifikasi Weighted Round Robin (PowerShell)
```powershell
1..8 | ForEach-Object {
    $r = Invoke-WebRequest -Uri http://localhost | ConvertFrom-Json
    Write-Host "Request $_`: $($r.server) | host: $($r.hostname)"
}
```

Expected output (pola 3:1):
```
Request 1: Server 1 - TokoKita | host: <backend1-hostname>
Request 2: Server 1 - TokoKita | host: <backend1-hostname>
Request 3: Server 1 - TokoKita | host: <backend1-hostname>
Request 4: Server 2 - TokoKita | host: <backend2-hostname>
Request 5: Server 1 - TokoKita | host: <backend1-hostname>
...
```
