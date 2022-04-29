import prisma from "@prisma/client";

const { PrismaClient } = prisma;

export const Prisma = new PrismaClient();
