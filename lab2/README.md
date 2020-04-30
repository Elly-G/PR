 
• Scopul protocolului SMTP

SMTP este un protocol simplu de transfer de mail( Simple Mail Transfer Protocol). Serverul SMTP este responsabil pentru trimiterea mesajelor. Sarcina sa, de regulă, constă din două funcții principale:
- verificarea setărilor și emiterea permisiunilor către computerul care încearcă să trimită un mesaj de e-mail;
- trimiterea unui mesaj de ieșire la adresa specificată și confirmarea trimiterii cu succes a mesajului. Dacă livrarea nu este posibilă, serverul returnează un răspuns cu o eroare de trimitere către expeditor

• Cum se poate verifica dacă serverul SMTP funcționează utilizînd linia de comandă?

În această problema Telnet este utilizat pe scară largă pentru a verifica conexiunile SMTP nereusite.
Cel mai frecvent mod de a verifica SMTP din linia de comandă este utilizarea comenzilor telnet, openssl sau ncat (nc). Aceasta este și cea mai cunoscută modalitate de testare a SMTP Relay. 
Protocolul telnet este folisit pentru a crea legătura cu un host.
 ncat sau nc  este un instrument universal CLI utilizat pentru scanarea porturilor, instrumentelor de securitate și intrumentelor de monitorizare.
 openssl este o biblioteca cu scot general care asigura punerea în aplicare a protocoalelor SSL și TLS open source.

• Care sunt comenzile SMTP

HELO – se indica domain name astfel incat mail server sa stie cine esti.
MAIL – se introduce adresa de e-mail a expeditorului.
RCPT – se precizeaza destinatarul/receptorul
DATA – se executa aceasta comanda inainte de a trimite corpul mesajului 
QUIT – se incheie conversatia cu serverul
EXPN – se indica ca destinataru/receptorul este mailing list
HELP – se solicita ajutorul de la mail server
NOOP – nu face alt ceva decat sa primeasca raspuns de la server
RSET – intrerupe conversatia curenta si incepe conversatia noua
SEND – trimite mesaj catre user’s terminal in loc de mailbox
SAML – trimite mesaj catre user’s terminat si user’s mailbox
SOML – trimite mesaj catre user’s terminal daca este conectat, altfel trimite mesajul la user’s mailbox
TURN – schimba rolul clientului  serverului. Este util, daca client program poate intra in rolul de server si trebuie sa primeasca mail de la computer remote.
VRFY – verifica daca exista un anumit utilizator cu adresa e-mail specificata.

• Pentru ce este nevoie de MUA, MSA, MTA și MDA

MUA (Mail User Agent)  este un program specializat pentru managementul mesajelor e-mail.
Acesta poate transmite si primi mesaje si poate filtra mesajele in functie de anumite criterii. 
MUA interactioneaza direct cu MTA pentru transmiterea mesajelor si citirea mesajelor folosind POP3 sau IMAP.
MTA (Mail Transfer Agent) este un software care transfera mesajele de posta electronica de la un calculator la altul folosind SMTP.
MSA (Mail Submission Agent) este un program de calculator sau un agent software care primeste mesajele de posta electronica de la un MUA si coopereaza cu MTA pentru livrarea mesajului. Utilizeaza ESMTP (Extended SMTP).
MDA (Mail Delivery Agent) este computer software component care este responsabil pentru livrarea de mesaje prin e-mail, catre mailboxul destinatarului local.

• Care este diferența dintre porturile 25, 465 și 587 ?

Port 25 - este portul necriptat SMTP-default
Port 2525 - acest port se deschide pe toate serverele SiteGround dacă portul 25 este filtrat (de exemplu, de către furnizorul de servicii Internet) și doriți să trimiteți e-mailuri necriptate prin SMTP
Portul 465 - acest port este utilizat pentru mesagerie securizată, folosind SMTP.

• Care este diferența dintre porturile 110 și 995 ?

Port 110 - acesta este portul necriptat POP3 implicit
Port 995 - acesta este portul pe care trebuie să-l utilizați dacă doriți să vă conectați folosind POP3 securizat.

• Care este diferența dintre porturile 143 și 993 ?

Portul 143 este portul IMAP necriptat implicit.
Portul 993 este portul care este utilizat pentru conexiune sigură prin IMAP.

• Cum funcționează protocolul SMTP ?

Clientul SMTP, adică expeditorul, descarcă e-mailul pe serverul SMTP, adică pe serverul de e-mail de ieșire al furnizorului de e-mail corespunzător. Acest lucru se realizează folosind o aplicație de e-mail bazată pe web într-un browser sau un program de e-mail (tehnic numit agent utilizator de e-mail, prescurtat MUA), cum ar fi Windows Live Mail sau Mozilla Thunderbird.
Serverul SMTP comunică apoi cu serverul DNS, iar acest server caută apoi adresa IP a serverului SMTP țintă (numit și „agent de livrare prin poștă”, prescurtat MDA), care este stocat pentru adresa destinatarului de e-mail.
Serverul SMTP trimite e-mail către serverul SMTP țintă printr-unul sau mai mulți „agenți de transfer de poștă” (MTA). Fiecare dintre aceste procese de redirecționare se realizează în conformitate cu protocolul SMTP.
Serverul SMTP țintă stochează temporar e-mailul în message store.
Destinatarii MUA descarcă e-mailuri prin IMAP sau POP3.

• Scopul protocoalelor POP3 și IMAP

Post Office Protocol version 3 (POP3) este un protocol poștal standard utilizat pentru a primi e-mail de la un server de la distanță către un client de poștă electronica local. POP3 permite descărcarea de e-mailuri pe computerul local și citirea  chiar și offline. Când se utilizeaza POP3 pentru conectare la un cont de e-mail, mesajele sunt descărcate local și șterse de pe serverul de e-mail. Unul în avantaje, dacă utilizeaza  POP3, mesajele  sunt stocate pe computerul  local/remote, ceea ce reduce spațiul pe care contul de e-mail îl utilizează pe serverul web.

The Internet Message Access Protocol (IMAP) este un protocol de poștă utilizat pentru a accesa e-mailurile pe un server web de la un client local. IMAP și POP3 sunt cele mai frecvent utilizate protocoale de poștă electronica pentru primirea e-mailului.

• Diferența dintre POP3 și IMAP

IMAP este benefic in utilizarea mai multor dispozitive pentru a verifica, raspunde si trimite e-mail. Toate modificarile care sunt realizate pe e-mail si pe contul de e-mail, sunt sincroniztae cu serverul mail si toate dispozitivele utilizate pe acelasi cont de e-mail In cazul in care se intampla ceva cu dispozitivele utilizate, un avantaj important este faptul ca originalele sunt pe servarul mail.
POP asigura disponibilitatea tuturor e-mailurilor, inclusiv fisierelor daca nu exista acces la internet. E-mailurile sunt stocate local pe dispozitiv.

• Cum să verificați dacă există o adresă de e-mail fără a trimite un e-mail ?

Exista diferite online-instrumente precum, https://email-checker.net, http://mailtester.com , pentru a verifica, daca exista o adresa de posta electronica. Exista si servere cu plata pentru verificarea adresei e-mail valid. Pot fi folosite comenzi dig sau nslookup  pentru a cauta DNS pentru a afla detaliile serverului e-mail. 

• Diferență dintre SSL și TLS

SSL se refera la Secure Sockets Layer, in timp ce TLS se refera la securitatea stratului de transport. 
SSL utilizeaza Message Authentication Code (MAC) dupa criptarea fiecarui mesaj, in timp ce TLS, foloseste un cod de autentificare a mesajelor bazat pe hash HMAP dupa fiecare criptare a mesajelor.
Autentificarea mesajelor SSL conecteaza key details si datele aplicatiei intr-un mod special, in timp ce versiunea TLS se bazeaza pe un cod de autententificare a mesajelor HMAP bazat pe hash.
