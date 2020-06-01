** • Cum este formatat corpul unei cereri HTTP pentru o cerere HTTP de tip POST ? ** 

Când datele sunt trimise de către un browser după ce datele au fost completate într-o formă, acestea se vor trimite `URL encoded`, ca nume serializate = perechi de valori separate prin simboluri ampersand ( „&“).
`POST / HTTP/1.1`
`Host: foo.com`
`Content-Type: application/x-www-form-urlencoded`
`Content-Length: 13`

`say=Hi&to=Mom`

** • De unde știe un client HTTP ce tip de conținut trimite serverul HTTP ? **

Un client HTTP cunoaste tipul continutului din `content-type` . Care sunt diverse.
> Type application: application/java-archive , application/xml , application/json ...
> Type audio: audio/mpeg , audio/x-wav ...
> Type image: image/gif , image/png ...
> Type text: text/css , text/csv , text/plain ...

** • Cum decide un client dacă ar trebui să aibă încredere în certificatul unui server ? **

Un certificat SSL este un tip popular de certificat digital care leagă detaliile de proprietate ale unui server web (și site-ul web) la cheile criptografice. Aceste chei sunt utilizate în protocolul SSL / TLS pentru a activa o sesiune sigură între un browser și serverul web care găzduiește certificatul SSL. Pentru ca un browser să aibă încredere într-un certificat SSL și să stabilească o sesiune SSL / TLS fără avertismente de securitate, Certificatul SSL trebuie să conțină numele de domeniu al site-ului web care îl folosește, să fie emis de un CA de încredere și să nu fi expirat.

** • Care este problema principală cu certificatele autosemnate ? **

Cea mai mare problemă cu un certificat semnat de sine este un atac de catre alt om.

** • Conexiunea persistentă HTTP – care sunt principalele beneficii ? **

O conexiune persistentă este una care rămâne deschisă pentru o perioadă de timp și poate fi reutilizată pentru mai multe solicitări, economisind necesitatea unei noi "strângeri de mână" TCP și folosind capacitățile de îmbunătățire a performanței TCP. Această conexiune nu va rămâne deschisă pentru totdeauna: conexiunile inactiv sunt închise după un anumit timp (un server poate utiliza antetul Keep-Alive pentru a specifica o perioadă minimă de timp pentru care conexiunea trebuie menținută deschisă).

** • Ce este negocierea conținutului în HTTP și cum are loc ? **

Dacă un client nu are cunoștințe despre suportul unui server pentru HTTP / 2.0, acesta începe cu HTTP / 1.1 și încearcă o actualizare la HTTP / 2.0 după cum urmează:
```        
        GET /default.htm HTTP/1.1
        Host: server.example.com
        Connection: Upgrade
        Upgrade: HTTP/2.0
```        
Dacă serverul nu acceptă noul protocol, acesta va răspunde pur și simplu clientului folosind HTTP / 1.1:
```
        HTTP/1.1 200 OK
        Content-length: 243
        Content-type: text/html
```        
Dacă serverul trece la noul protocol, acesta va semnaliza printr-un răspuns 101. Serverul trece la HTTP / 2.0 imediat după linia goală care încheie răspunsul 101.
```
        HTTP/1.1 101 Switching Protocols
        Connection: Upgrade
        Upgrade: HTTP/2.0
        [ HTTP/2.0 frame ]     
```   

** • Care sunt tipurile de negociere a conținutului HTTP ? **

- Abbreviated handshake
- A full handshake

** • Ce este un ETag în HTTP și cum funcționează ? **

 HTTP ETag este un identificator pentru o versiune specifică a unei resurse. Acesta permite la cache să fie mai eficient și să economisească lățimea de bandă, deoarece un server web nu trebuie să retrimită un răspuns complet dacă conținutul nu s-a schimbat.

** • Diferența dintre protocoalele fără stare și cele cu stare. Cărui tip îi aparține HTTP ? **

Protocoalele cu stare se mai numesc si link-state routing algorithm, sunt protocoale cu preferarea drumului minim (SPF shortest path first),menţin o bază de date complexă a topologiei reţelei. Spre deosebire deprotocoalele fara stare, ele folosind starea legăturilor dezvoltă şi întreţin o cunoaştere completă a routerelor de reţea, ca şi a felului cum sunt interconectate acestea.
HTTP este un protocol cu stare.

** • Avantajele cheie ale HTTP/2 în comparație cu HTTP/1.1 **

HTTP/2 creștea considerabila a vitezei de încărcare a site-urilor pe desktop și pe telefoanele mobile, reducerea consumului de trafic internet, oferă securitate sporită.

** • Ce este un tip MIME, din ce constă și pentru ce se folosește ? **

MIME este un stardat care indica natura si formatul documentului, fisierului sau colectiei de biti. Este definit si standardizat  in IETF's RFC 6838.

** • Care este diferența dintre GET și POST ? **

GET este utilizat pentru expedierea informatiei catre server.
POST este utilizat pentru preluarea datelor de la server.

** • Care este diferența dintre PUT și POST ? **

PUT expediaza un mesaj sau un fisier catre un URI si daca este ocupat atunci este inlocuit cu informatia din PUT. Datelenu pot fi adaugate in cache.
POST expediaza catre URI si asteapta ca acesta sa prelucreze cererea, apoi serverul prelucreaza datele. Datele pot fi adaugate in cache.

** • Care sunt metodele idempotente în HTTP și care sunt scopul lor. **

Metodele idempotente în HTTP  sunt: OPTIONS, GET, HEAD, PUT, DELETE.
Mai multe cereri identice vor conduce la returnarea aceluiași răspuns

** • Cum sunt identificate resursele în protocolul HTTP ? **

` <protocol>://<nume_DNS>/<nume_local> `
    `protoco`l - este protocolul folosit (de cele mai multe ori http)
    `nume_DNS` - este numele domeniului pe care se află resursa
    `nume_local` - este format din calea și numele resursei de pe discul local

** • Care sunt metodele sigure și nesigure în HTTP ? **

Sigure:
> GET
> HEAD

Nesigure:
> POST
> PUT
> DELETE


** • Pentru ce este nevoie de cURL ? **

Pentru  a efectua HTTP request-uri din consola.

** • Pentru ce este nevoie de HTTP Proxy? **

Proxy HTTP este special creat pentru conexiunile HTTP, dar poate fi folosit și pentru alte protocoale.

Browserul (CLIENT) trimite ` GET http: // SERVER / calea HTTP / 1.1 către PROXY ` 
Acum PROXY va trimite solicitarea reală către SERVER.
SERVER-ul va vedea doar PROXY ca conexiune și răspunde la PROXY la fel ca la un CLIENT.
PROXY primește răspunsul și îl transmite înapoi CLIENTULUI.

** • Diferența dintre autentificare și autorizare? **

Autentificarea este procesul de verificare a detaliilor unui utilizator pentru identificarea acestuia și acordarea accesului la sistem.
Autorizarea este procesul de verificare a privilegiilor sau permisiunilor utilizatorului autentificat pentru a accesa resursele sistemului.

** • Care sunt metodele de autentificare HTTP ? **

Autentificare simpla(Basic authentification), HTTP SSL Certificate Mapping, autentificare prin proxy,  HTTP NTLMSSP Authentification, HTTP GSS-API/SSPI authentification using SPENGO and Kerberos

** • Modalități de identificare a utilizatorilor în HTTP **

> HTTP request headers
> IP address
> Long URLs
> Cookies
> Login information (authentication)


** • HTTP cookies – pentru ce se folosește ? **

Cu ajutorul cookies serverul reține faptul că utilizatorul s-a autentificat, și îi va permite acțiuni specifice celor autentificați, de asemena cookies ajuta la setarea preferintelor utilizatorului si pastrarea acestora dupa finisarea sesiunii
