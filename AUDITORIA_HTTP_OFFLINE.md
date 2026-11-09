# Auditoria V8 — HTTP, offline, persistência e mobile

- **HTTP_real:** BLOQUEADO: Chromium ERR_BLOCKED_BY_ADMINISTRATOR em localhost
- **offline_browser:** NÃO VALIDADO: não foi possível iniciar origem HTTP
- **persistence_after_restart:** NÃO VALIDADO em navegador real
- **mobile_real_device:** NÃO EXECUTADO: não há acesso a iPhone físico
- **mobile_emulation:** NÃO EXECUTADO na origem HTTP bloqueada
- **static_assets:** 9 PNGs e 5 cenários presentes
- **phase_3_approval:** PENDENTE

Não declarar aprovação de testes bloqueados. Para testar no iPhone, hospedar o pacote em HTTPS e usar Safari; para offline completo, implementar service worker e cache de app shell antes de validar.
