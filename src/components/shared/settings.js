export const SETTINGS = {
    jsonbin: "https://api.jsonbin.io/b/61cad7b3c277c467cb377947",
    product_profiles:3,
    n_attributes:9,
    n_questions:15 ,

    it: {
        attributes: {
            0: "Regista",
            1: "Tipologia",
            2: "Personaggi",
            3: "Genere",
            4: "Location",
            5: "Collocazione temporale",
            6: "Saga",
            7: "Durata",
            8: "Prima visione",
        },
        mask:{
            0: {0:'Christopher Nolan', 1:'Tim Burton', 2:'Steven Spielberg'},
            1: {0:'Film d\'animazione', 1:'Live-action'},
            2: {0:'Esseri umani', 1:'Animali', 2:'Robot/androidi/umanoidi'},
            3: {0:'Fantascienza', 1:'Thriller', 2:'Avventura'},
            4: {0: 'Stati Uniti d\'America', 1:'Europa', 2:'Giappone', 3:'Marte'},
            5: {0:'Fine 1800', 1:'2022', 2:'2100'},
            6: {0:'Sì', 1:'No'},
            7: {0:'1h e 40min', 1:'2h', 2:'2h e 20min'},
            8: {0:'Cinema', 1:'Piattaforme'},
        }
    },

    // ENGLISH
    en: {
        attributes: {
            0: "Director",
            1: "Type",
            2: "Characters",
            3: "Genre",
            4: "Location",
            5: "Temporal collocation",
            6: "Saga",
            7: "Duration",
            8: "First viewing",
        },
        mask:{
            0: {0:'Christopher Nolan', 1:'Tim Burton', 2:'Steven Spielberg'},
            1: {0:'Animation film', 1:'Live-action'},
            2: {0:'Humans', 1:'Animals', 2:'Robots/androids/humanoids'},
            3: {0:'Science-fiction', 1:'Thriller', 2:'Adventure'},
            4: {0: 'United States of America', 1:'Europe', 2:'Japan', 3:'Mars'},
            5: {0:'End of the 19th century', 1:'2022', 2:'2100'},
            6: {0:'Yes', 1:'No'},
            7: {0:'1h 40min', 1:'2h', 2:'2h 20min'},
            8: {0:'Cinema', 1:'Platforms'},
        }
    },
};
