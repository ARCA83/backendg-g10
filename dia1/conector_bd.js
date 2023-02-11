import prisma from '@prisma/client'

// asi se exporta de manera por defecto
export default new prisma.PrismaClient({
    log:['query'],
})

