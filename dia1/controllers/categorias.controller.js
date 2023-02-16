import conexion from "../conector_bd.js";

export const crearCategoria = async(req, res) => {
  const { body } = req;
  console.log(body);
  // si es que la creacion es exitosa
  // de manera asincrona

  const respuesta = await conexion.categoria.create({
    data: {
      nombre: body.nombre,
    },
  });

  res.json({
    message: "Se creo la categoria exitosamente",
    content: respuesta,
  })
};

export const listarCategorias = async(req,res)=>{
    // SELECT * FROM categorias
    const respuesta =await conexion.categoria.findMany()

    res.json({
        content:respuesta,
    })
};

export const buscarCategoriasPorid = async(req, res)=>{
    console.log(req.params)
        const {id}=req.params
        const resultado =await conexion.categoria.findFirst({where: {id:+id}})
        if(!resultado){
            return res.json({
                message:'Categoria no existe',
            })
        }
    // no se puede enviar dos o mas respuestas al cliente porque la conexion  ya termino    
        else{
        return res.json({
            content:resultado,
        })
    }
}
export const actualizarCategoria = async(req,res)=>{
    const {id}= req.params
    const {body}=req
    //buscar primero si la categoria existe, si no existe retornar un message diciendo que no existe

    const categoria = await conexion.categoria.findFirst({
        data:{nombre:body.nombre},where:{id:+id}
    })
    if (!categoria) {
      return res.json({
        message: "La Categoria no existe",
      });
    }
     else{
    return res.json({
        content: resultado,
    })
    }
    }
export const eliminarCategoria=async(req,res)=>{
    const { id } = req.params
    const categoriaEncontrada=await conexion.categoria.findFirst({ where: { id: +id } })
    if (!categoriaEncontrada){
        return res.json({
            message:'La categoria no existe',
        })
    }
    await conexion.categoria.delete({where:{id:+id}})

    return res.json({
        message:'Categoria eliminada exitosamente',
    })
}