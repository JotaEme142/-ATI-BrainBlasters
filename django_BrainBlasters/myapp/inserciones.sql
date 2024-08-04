--Insercion de las categorias:
INSERT INTO myapp_categoria (id, nombre) VALUES (1, 'Deportes');
INSERT INTO myapp_categoria (id, nombre) VALUES (2, 'Geografía');
INSERT INTO myapp_categoria (id, nombre) VALUES (3, 'Historia');
INSERT INTO myapp_categoria (id, nombre) VALUES (4, 'Política');
INSERT INTO myapp_categoria (id, nombre) VALUES (5, 'Arte');
INSERT INTO myapp_categoria (id, nombre) VALUES (6, 'Celebridades');
INSERT INTO myapp_categoria (id, nombre) VALUES (7, 'Animales');



-- Insercion de las preguntas en la categoría 21

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (1, 1, "¿Quién es el máximo goleador de la Premier League del Manchester United?", 
        "Sir Bobby Charlton", "Ryan Giggs", "David Beckham", "Wayne Rooney", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (1, 1, "¿En qué deporte compite Fanny Chmelar por Alemania?", 
        "Natación", "Salto ecuestre", "Gimnasia", "Esquí", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (1, 1, "¿Quién es frecuentemente llamado 'el Maestro' en el circuito de tenis masculino?", 
        "Bill Tilden", "Boris Becker", "Pete Sampras", "Roger Federer", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (1, 1, "¿En qué año ganaron los New Orleans Saints el Super Bowl?", 
        "2008", "2009", "2011", "2010", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (1, 1, "En un juego de snooker, ¿de qué color es la bola que vale 3 puntos?", 
        "Amarillo", "Marrón", "Azul", "Verde", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (1, 1, "En la Copa Mundial de la FIFA 2014, ¿cuál fue el marcador final en el partido Brasil - Alemania?", 
        "1-5", "1-6", "2-6", "1-7", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (1, 1, "¿Qué luchador profesional cayó desde las vigas y murió durante un evento en vivo de Pay-Per-View en 1999?", 
        "Chris Benoit", "Lex Luger", "Al Snow", "Owen Hart", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (1, 1, "¿Qué ciudad tiene todas las camisetas de sus equipos deportivos profesionales con el mismo esquema de colores?", 
        "Nueva York", "Seattle", "Tampa Bay", "Pittsburgh", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (1, 1, "¿Quién ganó el Campeonato Mundial de Pilotos de Fórmula Uno en 2017?", 
        "Sebastian Vettel", "Nico Rosberg", "Max Verstappen", "Lewis Hamilton", 4);

-- Insercion de las preguntas en la categoría 22

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (2, 1, "¿Cuál de los siguientes no es un país megadiverso, uno que alberga un gran número de especies endémicas de la tierra?", 
        "Perú", "México", "Sudáfrica", "Tailandia", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (2, 1, "¿Cuál es la isla no continental más grande del mundo?", 
        "Nueva Guinea", "Borneo", "Madagascar", "Groenlandia", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (2, 1, "¿Cuál de estos países limita con Polonia?", 
        "Francia", "Noruega", "Países Bajos", "Lituania", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (2, 1, "¿Cuáles dos países modernos solían ser conocidos como la región de Rodesia entre la década de 1890 y 1980?", 
        "Togo y Benín", "Lesoto y Suazilandia", "Ruanda y Burundi", "Zambia y Zimbabue", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (2, 1, "¿Qué evento llevó a Liechtenstein a agregar una corona a su bandera?", 
        "Coronación del Príncipe Johann I Joseph en 1805", "Decreto de Carlos VI en 1719", "Firma de la Constitución de Liechtenstein en 1862", "Los Juegos Olímpicos de 1936", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (2, 1, "¿Cuál es la capital de Corea del Sur?", 
        "Pionyang", "Taegu", "Kitakyushu", "Seúl", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (2, 1, "¿Montreal está en qué provincia canadiense?", 
        "Ontario", "Nueva Escocia", "Alberta", "Quebec", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (2, 1, "¿En qué ciudad se encuentra el Ejército de Terracota?", 
        "Beijing", "Shanghái", "Hong Kong", "Xi'an", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (2, 1, "¿En qué país europeo se encuentra la sede de la Organización Mundial de la Salud?", 
        "Reino Unido", "Francia", "Bélgica", "Suiza", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (2, 1, "¿El distrito japonés Akihabara también es conocido por qué apodo?", 
        "Río Moon Walk", "Centro Otaku", "Ojos Grandes", "Ciudad Eléctrica", 4);

-- Insercion de las preguntas en la categoría 23

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (3, 1, "¿Cuál de los siguientes países no fue una potencia del Eje durante la Segunda Guerra Mundial?", 
        "Italia", "Alemania", "Japón", "Unión Soviética", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (3, 1, "¿Cómo fue ejecutado Sócrates?", 
        "Decapitación", "Pelotón de fusilamiento", "Crucifixión", "Veneno", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (3, 1, "¿Cómo se llamó la transferencia de enfermedades, cultivos y personas a través del Atlántico poco después del descubrimiento de las Américas?", 
        "Comercio triangular", "Tráfico transatlántico de esclavos", "La ruta de la seda", "El intercambio colombiano", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (3, 1, "¿Quién fue el presidente de los Estados Unidos durante la Guerra de 1812?", 
        "James Monroe", "Thomas Jefferson", "Andrew Jackson", "James Madison", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (3, 1, "¿Qué batalla de la Segunda Guerra Mundial tuvo el mayor número de bajas?", 
        "Batalla de Normandía", "Batalla de Berlín", "Batalla de Midway", "Batalla de Stalingrado", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (3, 1, "¿En qué guerra luchó América del Norte desde 1950 hasta 1953?", 
        "Primera Guerra Mundial", "Segunda Guerra Mundial", "Guerra de Vietnam", "Guerra de Corea", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (3, 1, "¿Quién fue el presidente de los Estados Unidos antes de George W. Bush?", 
        "Ronald Reagan", "George H. W. Bush", "Jimmy Carter", "Bill Clinton", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (3, 1, "¿En qué año se firmó la Declaración de Independencia de los Estados Unidos?", 
        "1775", "1777", "1778", "1776", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (3, 1, "¿Quién escribió 'Mein Kampf'?", 
        "Joseph Goebbels", "Hermann Göring", "Heinrich Himmler", "Adolf Hitler", 4);


-- Insercion de las preguntas en la categoría 24

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (4, 1, "¿Cuál de estos fue un candidato oficial en las Elecciones Generales Británicas de 2017?", 
        "James Francis", "Robert Wimbledon", "Sir Crumpetsby", "Lord Buckethead", 4);




INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (4, 1, "Antes de 2016, ¿en qué otro año se postuló Donald Trump para Presidente?", 
        "2012", "1988", "2008", "2000", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (4, 1, "¿Quién sucedió a Joseph Stalin como Secretario General del Partido Comunista de la Unión Soviética?", 
        "Leonid Brezhnev", "Mikhail Gorbachev", "Boris Yeltsin", "Nikita Khrushchev", 4);


INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (4, 1, "Antes de 2011, 'True Capitalist Radio' se conocía con otro nombre. ¿Cuál era ese nombre?", 
        "True Republican Radio", "Texan Capitalist Radio", "United Capitalists", "True Conservative Radio", 4);


INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (4, 1, "¿Qué presidente de EE.UU. recibió el apodo de 'Teddy' después de negarse a disparar a un oso negro indefenso?", 
        "Woodrow Wilson", "James F. Fielder", "Andrew Jackson", "Theodore Roosevelt", 4);

-- Insercion de las preguntas en la categoría 25

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (5, 1, "¿Cuál es el nombre del arte japonés de doblar papel en formas y figuras decorativas?", 
        "Sumi-e", "Ukiyo-e", "Haiku", "Origami", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (5, 1, "¿Quién pintó el fresco bíblico 'La Creación de Adán'?", 
        "Leonardo da Vinci", "Caravaggio", "Rembrandt", "Miguel Ángel", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (5, 1, "¿Quién diseñó el logo de Chupa Chups?", 
        "Pablo Picasso", "Andy Warhol", "Vincent van Gogh", "Salvador Dalí", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (5, 1, "¿Quién pintó la Capilla Sixtina?", 
        "Leonardo da Vinci", "Pablo Picasso", "Rafael", "Miguel Ángel", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (5, 1, "¿Qué estilo de artista usaba pequeños puntos de diferentes colores para crear una imagen?", 
        "Paul Cézanne", "Vincent Van Gogh", "Henri Rousseau", "Georges Seurat", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (5, 1, "¿Quién pintó el épico mural 'Guernica'?", 
        "Francisco de Goya", "Leonardo da Vinci", "Henri Matisse", "Pablo Picasso", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (5, 1, "¿Quién pintó 'La noche estrellada'?", 
        "Pablo Picasso", "Leonardo da Vinci", "Miguel Ángel", "Vincent van Gogh", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (5, 1, "¿El cuadro 'La noche estrellada' de Vincent van Gogh era parte de qué movimiento artístico?", 
        "Romanticismo", "Neoclasicismo", "Impresionismo", "Postimpresionismo", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (5, 1, "¿Qué escultor francés diseñó la Estatua de la Libertad?", 
        "Jean-Léon Gérôme", "Auguste Rodin", "Henri Matisse", "Frédéric Auguste Bartholdi", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (5, 1, "¿El lugar de nacimiento y de muerte de Albrecht Dürer fue en...", 
        "Augsburg", "Bamberg", "Berlín", "Núremberg", 4);

-- Insercion de las preguntas en la categoría 26

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (6, 1, "¿Neil Hamburger es interpretado por qué comediante?", 
        "Nathan Fielder", "Tim Heidecker", "Todd Glass", "Gregg Turkington", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (6, 1, "¿Por qué nombre es mejor conocido Carlos Estevez?", 
        "Ricky Martin", "Bruno Mars", "Joaquín Phoenix", "Charlie Sheen", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (6, 1, "¿De qué estado de EE.UU. es originario Billy Herrington?", 
        "Arizona", "California", "Georgia", "Nueva York", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (6, 1, "¿Qué celebridad estadounidense murió en 1977 jugando al golf en La Moraleja, Madrid?", 
        "Elvis Presley", "Charlie Chaplin", "Groucho Marx", "Bing Crosby", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (6, 1, "¿Cuánto peso perdió Chris Pratt para su papel como Star-Lord en 'Guardianes de la Galaxia'?", 
        "30 lbs", "50 lbs", "70 lbs", "60 lbs", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (6, 1, "¿Cuál fue la causa del suicidio de Marilyn Monroe?", 
        "Ataque con cuchillo", "Incendio en casa", "Disparo", "Sobredosis de drogas", 4);


INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (6, 1, "¿En qué suele centrarse el cineasta Dan Bell en sus películas?", 
        "Monumentos históricos", "Películas de acción", "Documentales", "Edificios abandonados y centros comerciales cerrados", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (6, 1, "¿Por qué nombre es mejor conocido Ramón Estevez?", 
        "Charlie Sheen", "Ramón Sheen", "Emilio Estevez", "Martin Sheen", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (6, 1, "¿Dónde nació Kanye West?", 
        "Chicago, Illinois", "Los Ángeles, California", "Detroit, Michigan", "Atlanta, Georgia", 4);

-- Insercion de las preguntas en la categoría 27

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (7, 1, "¿Qué tipo de criatura es un Bonobo?", 
        "León", "Perico", "Gato salvaje", "Simio", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (7, 1, "¿Qué raza de perro es una de las más antiguas y ha prosperado desde antes del 400 a.C.?", 
        "Bulldogs", "Boxers", "Chihuahua", "Pugs", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (7, 1, "¿De qué están hechos los cuernos de rinoceronte?", 
        "Hueso", "Marfil", "Piel", "Queratin", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (7, 1, "¿Cuál es el nombre de una abeja macho que proviene de un huevo no fertilizado?", 
        "Soldado", "Trabajador", "Macho", "Drone", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (7, 1, "¿Cuántos dientes tiene un conejo adulto?", 
        "30", "26", "24", "28", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (7, 1, "¿Cuál es el nombre de la morada de un conejo?", 
        "Nido", "Cueva", "Dray", "Burrow", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (7, 1, "¿Cuál es el animal más rápido?", 
        "Águila dorada", "Chita", "Mosca de caballo", "Halcón peregrino", 4);

INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
VALUES (7, 1, "¿Hippocampus es el nombre en latín de qué criatura marina?", 
        "Delfín", "Ballena", "Pulpo", "Caballito de mar", 4);

--TRIVIAS DE VERDADERO Y FALSO

-- INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
-- VALUES (4, 0, "Dinamarca tiene un monarca.", 
--         "Verdadero", "Falso", NULL, NULL, 1);

-- INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
-- VALUES (4, 0, "Durante las elecciones presidenciales de 2016 en Estados Unidos, el Estado de California poseía la mayor cantidad de votos electorales, con 55.", 
--         "Verdadero", "Falso", NULL, NULL, 1);

-- INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
-- VALUES (4, 0, "El Estado de Queensland, Australia votó NO en un referéndum sobre el horario de verano en 1992.", 
--         "Verdadero", "Falso", NULL, NULL, 1);

-- INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
-- VALUES (4, 0, "Donald Trump ganó el voto popular en las elecciones presidenciales de 2016 en Estados Unidos.", 
--         "Falso", "Verdadero", NULL, NULL, 1);

-- INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
-- VALUES (4, 0, "Jeb Bush fue elegido Gobernador de Florida en 2002, comenzando su carrera política.", 
--         "Falso", "Verdadero", NULL, NULL, 1);

-- INSERT INTO myapp_trivia (categoria_id, tipo, pregunta, opcion_txt1, opcion_txt2, opcion_txt3, opcion_txt4, respuesta) 
-- VALUES (6, 1, "¿Cuánto mide Tom Cruise?", 
--         "5' 9\"", "5' 4\"", "5' 5\"", "5' 7\"", 4);
