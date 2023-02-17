import mongoose from "mongoose";
import { validarToken } from "../utils/validador.js";

// Data Types de Mongoose >
// Configuaracion d las columnas >
// NOTA: Todas estas configuraciones solo sirven para mongoose
const usuarioSchema = new mongoose.Schema(
  {
    nombre: {
      type: mongoose.Schema.Types.String,
      require: true,
      maxLength: 50,
    },
    apellido: {
      type: mongoose.Schema.Types.String,
      maxLength: 50,
    },
    correo: {
      type: mongoose.Schema.String,
      required: true,
      index: true,
      unique: true,
    },
    password: {
      type: mongoose.Schema.String,
      required: true,
      set: (valor) => {
        //servira para cuando queramos modificar o establecer el valor de esta propiedad
        console.log(valor);
        return "123";
      },
    },
  },
  //Configuraciones de la coleccion
  {
    timestamps: {
      createdAt: true,// se registre un nuevo usuario tomara la hora base de datos
      updatedAt: "actualizado",// se actualice alguna informacion de un usuario cambiara su hora y fecha a la hora actual de la base de datos
    },
  }
);

export const UsuarioModel = mongoose.model('usuarios',usuarioSchema);