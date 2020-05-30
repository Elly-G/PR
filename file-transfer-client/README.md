** Ce este un protocol orientat către tranzacții, fără conexiune ? **

Protocolul orientat catre tranzactii, fara conexiune, reprezinta un protocol care nu asteapta raspuns de la client, adica nu tine cont de pachetele pierdute, daca internetul este de calitate buna atunci pachetele o sa fie transmise toate cu bine, daca conexiunea este rea atunci o sa fie pierderi de pachete.

** Ce tipuri de aplicații beneficiază în general de utilizarea protocolului UDP ? **

Desktop sharing(teamviewer, VoIP, video streaming, Skype

** De ce protocolul UDP nu garantează că datele vor fi transmise cu succes ? **

Absența autentificării reciproce între emitator și receptor asigură o viteză excelentă de transmitere a UDP - cu toate acestea, protocolul nu poate garanta nici completitudinea, nici securitatea pachetelor de date

** Diferența dintre blocking si non-blocking sockets **

Blocking sockets: presupune faptul ca doar un singur soacket poate fi deschis in orice moment intr-un thread, nu este la fel de eficient ca non-blocking fiindca avem nevoie de un nou fir de executie pentru fiecare socket.
Non-blocking sockets: putem gestiona un numar mult mai mare de clienti


** În protocolul TCP există Three Way Handshake, de ce în UDP nu există ? **

UDP nu gestioneaza pachetele in vreun fel careva el doar expediaza datele catre destinatar

** Numiti cele 2 apeluri de sistem necesare pentru a crea un server UDP **

UDP Server :

    Create UDP socket.
    Bind the socket to server address.
    Wait until datagram packet arrives from client.
    Process the datagram packet and send a reply to client.
    Go back to Step 3.

UDP Client :

    Create UDP socket.
    Send message to server.
    Wait until response from server is recieved.
    Process reply and go back to step 2, if necessary.
    Close socket descriptor and exit.


** Care este rolul metodei bind() ? **

Leaga socketul de adresa Serverului

** Care este rolul metodelor sendto() și recvfrom() ? **

`sendto()` Trimiterea datelor catre client sau server
`recvfrom()` primirea datelor de la server sau client

** Care este dimensiunea antetului unui pachet UDP în octeți ? **

4 octeți

** Într-o conexiune UDP, clientul sau serverul trimite mai întâi datele ? **

Yes

** Care este adresa de loopback IPv6 și care este rolul ei ? ** 

`0000:0000:0000:0000:0000:0000:0000:0001/128 `
O interfață loopback este utilă pentru sarcinile de depanare, adică un nod trimite packete către sine însuși.

** Datele primite prin recvfrom() au întotdeauna aceeași dimensiune cu datele trimise cu sendto()? **

Depinde de calitatea conexiunii la internet, daca conexiunea este buna atunci dimensiunea va fi la fel daca conexiunea este rea atunci dimensiunea v-a fi diferita

** Este acceptabil să închei execuția programului dacă este detectată o eroare de rețea ? **

Daca afisam o eroare inainte de a inchide programul cu specificarea tipului erorii.

** De ce nu este folosit algoritmul Nagle în protocolul UDP ? **

Este un algoritm de imbunatatire a protocolului tcp/ip

** Ce instrumente listează socket-urile UDP deschise în sistemele de operare Windows și Linux ? **

>Linux- ss, netstat | grep "udp"
>Windows- netstat -an | find "UDP" | more

** Același program poate folosi UDP și TCP ? **

Yes 

** Diferența dintre aplicații UDP Unicast, Broadcast, și Multicast **

`Unicast` – point to point
`Multicast` – point to multiPoint
`Broadcast` – point to all points

** Ce face mai ușor multiplexarea cu UDP decît cu TCP ? **

Fiindca UDP nu tine cont de packetele expediate in retea pe cand TCP conexiunea persista intre packete.

** În protocolul UDP este un antet „Total length”, cum se calculează și care este rolul lui ?  **

8 octeți
Antetul UDP este un antet fix cu 8 biți și simplu, în timp ce pentru TCP poate varia de la 20 de octeți la 60 de octeți.

![ld0br](https://user-images.githubusercontent.com/48655276/83340253-7eae1a00-a2de-11ea-94e8-5514a8b928f4.png)

