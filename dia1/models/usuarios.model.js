import mongoose from "mongoose";
import bcrypt from "bcryptjs";

// Datatypes de mongoose > https://mongoosejs.com/docs/schematypes.html
// Configuracion de las columnas > https://mongoosejs.com/docs/schematypes.html#schematype-options
// NOTA: todas estas configuracion SOLAMENTE funcionaran en mongoose, es decir si agregamos data directamente en mongo ninguna de estas tendra validez

const usuarioSchema = new mongoose.Schema(
  {
    nombre: {
      type: mongoose.Schema.Types.String,
      required: true,
      maxLength: 50,
    },

    apellido: {
      type: mongoose.Schema.Types.String,
      maxLength: 50,
    },

    correo: {
      type: mongoose.Schema.Types.String,
      required: true,
      index: true,
      unique: true,
    },

    password: {
      type: mongoose.Schema.Types.String,
      required: true,
      set: (valor) => {
        // servira para cuando queramos modificar o establer el valor de esta propiedad
        const passwordHashed= bcrypt.hashSync(valor, 10)
        console.log(valor);
        return passwordHashed;
      },
    },
    //Creando la referencia entre mis usuarios y mis calendarios aen la cual solamente guardaaremos el id de ese calendario y no toda la informacion
    calendarios:{
      type:[mongoose.Schema.Types.ObjectId],
      // type [calendarioSchema]> si hubieramos realizado de esta manera estariamos indicando que dentro del modelo de usuario se almacenara toda la informacion del calendario y todo se guardaria een el mismo modelo del usuario cos que no es pertinente para este tipo de casos.
    },
    validado:{
      type: mongoose.Schema.Types.Boolean,
      default: false,
    }
  },
  // Configuraciones de la coleccion
  {
    timestamps: {
      createdAt: true,// se registro un nuevo usuario tomara la hora de la basde de datos
      updatedAt: "actualizado",// se actualice alguna informacion de un usuario cambiara su hora y fehca a la hora actual de la base de datos. 
    },
  }
);

export const UsuarioModel = mongoose.model("usuarios", usuarioSchema);
