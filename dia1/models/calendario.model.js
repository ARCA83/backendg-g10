import mongoose from "mongoose";


const diasSchema = new mongoose.Schema({
  dia: mongoose.Schema.Types.String,
  enum: ["LUN", "MAR", "MIE", "JUE", "VIE", "SAB", "DOM"],
},
{_id:false}// no se requiree crear el atributo _id para cuando se cree diasSchema
);

const calendarioScheema = new mongoose.Schema({
    titulo:{
        type: mongoose.Schema.Types.String,
        required: true,
        
      },
      descripcion: mongoose.Schema.Types.String,
      hora_inicio:{
        validator:{
            validator: (valor)=>{
                return/([0-2][0-9]:[0-5][0-9])/.test(valor);
            },
            message: "El formato debe ser desde 00:00 hasta 23:59"
        },
      },
      hora_fin: mongoose.Schema.Types.String,
      dias:{
        type:[diasSchema],
      },
});

export const CalendarioModel = mongoose.model("calendarios",calendarioScheema)