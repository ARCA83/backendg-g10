import { Router } from "express";
import * as calendariosController from "../controllers/calendarios.controllers.js";


export const calendariosRouter = Router();

//calendariosRouter.get(
//    "/calendarios",
//    validarToken,
//    calendariosController.devolverCalendarios
//);
//
//calendariosController.post(
//    "/calendarios",
//    validarToken,
//    calendariosController.crearCalendario
//);

calendariosRouter
  .route("/calendarios")
  .post( calendariosController.crearCalendario)
  .get(calendariosController.devolverCalendarios);

  // En la cual tambien se repetira el mismo middleware y se tiene configurar por cada metodo HTTP de manera independiente
//calendariosRouter
//  .route("/calendarios")
//  .post(validarToken, calendariosController.crearCalendario)
//  .get(validarToken, calendariosController.devolverCalendarios);


calendariosRouter
.route("/calendario/:id")
.put(calendariosController.actualizarCalendario)
.delete(calendariosController.eliminarCalendario);