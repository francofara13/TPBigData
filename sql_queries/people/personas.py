#!/usr/bin/env python
# -*- coding: utf-8 -*-


FBIDMIO = "10204480128391078"

import urllib2, random, time, urllib, re
from unicodedata import normalize

nombre = ["juan","pedro","ramon","eber","agustin","marcelo","michael","santiago","jose","bruno","matias","nicolas","david","facundo","diego","ivan","julieta","manuel","ramiro","joaquin","daniel","marcela","nair","sofia","augusto","gerardo","samuel","ester","marcos","ricardo","julian","franco","victor","claudio","felix","fabian","carolina","gloria","silvia","antonio","cristina","esteban","selene","paula","florencia","luis","nahuel",
"damian","clemente","rafael","lucas","pablo","martin","natalia","luisa","sebastian","amado","carlos","guido","rocio","norma","enzo","andres","emilio","mateo","lorenzo","delfina","salvador","cintia","antonella","agostina","mariana","federico","virginia","hector","anibal","leandro","nestor","hugo","soledad"]

apellido = ["moreno","fernandez","martinez","toledi","suller","hoc","marchi","duran","bassi","bertoia","colussi","coria","bisio","badino","zbrun","schneider","kinsler","cervio","degiorgio","alba","anzardi","cattaneo","cejas","william","willener","lopez","hoz","nos","serruya","chiabotto","hein","bogino","faraudello","socin","cordoba","gaudio","muller","knoll","peretti","trevisan","ronzoni","rodiconda","rodriguez","velasquez","zenklusen","winchester","quinteros","pighin","pereyra","rubens","baxuer","torres","tolosa","torcivia","sudano","stradella","mendez","mansilla","morgan","gervasoni","muga","prodan","perone","panigo","montini","monzon","walter","biscarrondo","prieto","lanzini","iturbe","castillon","luna","barobero","bertoni","elsener","friedli","walker","aschieri","bertorello","daniele","montaner","karchesky","montu","molina","maina","lattina","keller","kaiser","trossero","trincheri","vico","viglietti","viale","pascuali","alonso","villa","orion","caruzzo","capria","braña","vangioni","balanta","botinelli","leguizamon","prida","vettorazi","marchisio","coronel","tapia","legrand",
"llopis","borras","valiente","giner","quirós","cabeza","souto","abellán","barranco","hervás","salguero","piñero","andrade","páez","amaya","olmo","haro","brito","arce","poveda","valles","salcedo", "mateu","serna","bartolomé","chaves","garzón","araujo","rebollo","noguera","del pozo","bonet","llorens","heras","pazos","avilés","lafuente","vives","alcalá","paniagua","sáenz","de miguel","ferrero","alcalde","alcázar", "tena","figueroa","solano","rosado","pena","zambrano","olmedo","mosquera","huerta","pla","calleja", "pizarro","frías","moyano","grande", "dorado","dávila","chamorro","criado", "freire","duque","valdés","tirado", "dos santos","espejo","rosales","portillo", "lobato","galván","tejero","gordillo", "real","gonzalo","llamas","agudo", "morillo","barrio","royo","melero", "alcaide","romera","jorge","cánovas", "fajardo","sainz","peinado","ariza", "carvajal","pavón","arjona","del valle", "duarte","toro","valenzuela",
"barbero", "guijarro","ruano","aznar","morcillo", "borrego","huertas","solé","segovia", "ferreiro","cerezo","godoy","estrada", "cebrián","alcántara","fraile","barragán", "catalán","falcón","castellanos","corrales", "egea","sastre","gámez","peralta", "campo","rovira","mejías","losada", "latorre","singh","alfaro","vergara", "bello","valls","granados","tapia", "navarrete","ocaña","pujol","ochoa", "becerra","vaquero","madrid","puente", "vélez","angulo","cervera","cuadrado", "cabezas","cobos","barreiro","coll", "ventura","barba","palma","pino", "muñiz","recio","cardona","arranz", "porras","belmonte","herranz","baena", "nicolás","lago","rincón","miralles", "casanova","sala","de la rosa","arévalo", "palomo","sanchís","cantero","castilla", "ballester","marrero","pineda","cid", "perea","cámara","bosch","quintero","salinas","grau", "pinto","solís","esteve","marques", "barrios","da silva","olivares","piñeiro", "carballo","luis","ayala",
"font", "sevilla","requena","peláez","alfonso", "prado","villegas","arribas","carbonell", "salgado","vela","moral","toledo", "zapata","llorente","saavedra","chacón","mohamed", "sola","riera","velázquez","alcaraz", "juárez","domenech","cárdenas","cobo", "correa","calero","ferreira","cáceres", "córdoba","andreu","rosa","hernando", "carrera","castellano","villa","chen", "clemente","carrión","aragón","roig", "sosa","bonilla","carretero","oliver", "burgos","leal","ojeda","amador", "linares","moran", "reina","paz", "villalba","mata", "naranjo","aguirre", "polo","caro", "lucas","valencia", "ramón","asensio", "mena","vallejo", "escribano","galindo", "domingo","arenas", "soria","aguado", "navas","pulido", "saiz","rojo", "cabello","puig", "alba","corral", "gimeno","ordoñez", "barrera","de la torre", "quesada","ros", "barroso","marco", "cuevas","martos", "montoya","de la cruz", "cuenca","murillo", "pozo","collado", "cordero","mas", "oliva",
"juan", "lorente", "rodrigo", "ponce", "bautista", "valle", "maldonado", "valverde", "ballesteros", "antón", "paredes", "bermejo", "salvador", "zamora", "castaño", "luna", "alarcón", "millán", "blasco", "escobar", "del rio", "mesa", "sancho", "lázaro", "de la fuente", "pons", "Ávila", "pacheco", "simón", "trujillo", "rueda", "hurtado", "tomas", "manzano", "cuesta", "villanueva", "guzmán", "serra", "salazar", "santamaría", "miguel", "bermúdez", "costa", "roca", "blázquez", "aranda", "acosta", "plaza", "jurado", "quintana", "salas", "conde", "gálvez", "abad", "calderón", "rico", "gracia", "padilla", "beltrán", "estévez", "rivero", "aparicio", "casas", "aguilera", "menéndez", "escudero", "mateos", "guillen", "miranda", "contreras", "villar", "mateo", "roldan", "heredia", "bueno", "macías", "guerra", "varela", "andrés", "benito", "pereira", "expósito", "palacios", "valero", "vila", "bernal", "robles", "mendoza", "soriano", "martí",
"marcos", "carrillo", "segura", "sierra", "ríos", "montes", "luque", "galán", "otero", "vera", "camacho", "rey", "arroyo", "redondo", "rivera", "casado", "silva", "rivas", "lara", "espinosa", "izquierdo", "franco", "merino", "pardo", "rojas", "gallardo", "bravo", "parra", "esteban", "moya", "soler", "velasco", "sáez", "soto", "román", "pastor", "crespo", "carmona", "vargas", "santiago", "arias", "benítez", "mora", "vicente", "duran", "ferrer", "giménez", "ibáñez", "montero", "hidalgo", "lorenzo", "santana", "herrero", "reyes", "pascual", "aguilar", "nieto", "caballero", "carrasco", "fuentes", "diez", "vega", "campos", "flores", "cabrera", "peña", "márquez", "herrera", "león", "cruz", "gallego", "vidal", "calvo", "méndez", "prieto", "cano", "guerrero", "lozano", "cortes", "castillo", "santos", "garrido", "medina", "núñez", "iglesias", "sanz", "marín", "rubio", "ortiz", "castro", "delgado", "ortega", "morales", "molina", "suarez",
"blanco", "serrano", "ramírez", "gil", "ramos", "vázquez", "domínguez", "torres", "navarro", "gutiérrez", "alonso", "romero", "muñoz", "Álvarez", "moreno", "díaz", "hernández", "ruiz", "jiménez", "martin", "gómez", "pérez", "sánchez", "martínez", "lópez", "fernández", "rodríguez", "gonzález", "garcía"]

localidad = [
            ["Santa Fe","Santa Fe","Rosario","Rafaela","Esperanza"],
            ["Cordoba","Cordoba","Carlos Paz","Capilla del monte","Cosquin"],
            ["Buenos Aires","La plata","Buenos Aires","Bahia Blanca","Mar del plata"],
            ["Entre Rios","Parana","Federeacion","Gualeguay","Gualeguaychu"],
            ["Mendoza","Mendoza","Godoy Cruz","Maipu","Rivadavia"],
            ["Neuquen","Neuquen","Cutral Co","Bariloche","Villa la angostura","San Martin de los Andes"],
            ["Tucuman","Concepcion","Simoca","Monteros","Ciudad de Yerba Buena"],
            ]

def remov(txt, codif='utf-8'):
    return normalize('NFKD', txt.decode(codif)).encode('ASCII','ignore').replace(" ","").replace(" ","")

class Persona:
    def __init__(self):
        self.nombre = nombre[random.randrange(0,len(nombre))].capitalize()
        self.apellido = apellido[random.randrange(0,len(apellido))].capitalize()

        il = random.randrange(0,len(localidad))

        self.provincia = localidad[il][0]
        self.localidad = localidad[il][random.randrange(01,len(localidad[il]))]

        self.telefono = random.randint(430000, 600000)

        te = random.randrange(1,5)

        if te==1:
            self.mail = self.nombre[0]+remov(self.apellido)+"@hotmail.com"
        elif te==2:
            self.mail = self.nombre[0:3]+"_"+remov(self.apellido)+"@gmail.com"
        elif te==3:
            self.mail = self.nombre[0]+remov(self.apellido)+str(random.randrange(100,999))+"@hotmail.com"
        elif te==4:
            self.mail = self.nombre+remov(self.apellido)+"@gmail.com"
        elif te==5:
            self.mail = self.nombre+"-"+remov(self.apellido)+"@hotmail.com"

        self.mail = self.mail.lower()
        self.dni = str(random.randrange(20,38))+str(random.randrange(123456,999999))
















