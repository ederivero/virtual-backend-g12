-- CreateEnum
CREATE TYPE "PEDIDO_ESTADO" AS ENUM ('CREADO', 'ACEPTADO', 'PAGADO', 'ERROR');

-- CreateEnum
CREATE TYPE "USUARIO_ROL" AS ENUM ('ADMINISTRADOR', 'CLIENTE');

-- CreateEnum
CREATE TYPE "UM_PRODUCTO" AS ENUM ('KG', 'UNIDAD');

-- CreateEnum
CREATE TYPE "CATEGORIA_PRODUCTO" AS ENUM ('VERDURA', 'FRUTA', 'ELECTRODOMESTICO', 'LIMPIEZA', 'OTROS');

-- CreateTable
CREATE TABLE "usuarios" (
    "id" SERIAL NOT NULL,
    "nombre" TEXT,
    "email" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    "rol" "USUARIO_ROL" NOT NULL DEFAULT E'CLIENTE',
    "validado" BOOLEAN NOT NULL DEFAULT false,

    CONSTRAINT "usuarios_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "productos" (
    "id" SERIAL NOT NULL,
    "nombre" TEXT NOT NULL,
    "precio" DOUBLE PRECISION NOT NULL,
    "unidad_medida" "UM_PRODUCTO" NOT NULL,
    "categoria" "CATEGORIA_PRODUCTO" NOT NULL,

    CONSTRAINT "productos_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "pedidos" (
    "id" SERIAL NOT NULL,
    "fecha" DATE NOT NULL,
    "total" DOUBLE PRECISION NOT NULL,
    "estado" "PEDIDO_ESTADO" NOT NULL,
    "process_id" TEXT,
    "cliente_id" INTEGER NOT NULL,

    CONSTRAINT "pedidos_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "detalle_pedidos" (
    "id" SERIAL NOT NULL,
    "cantidad" DOUBLE PRECISION NOT NULL,
    "sub_total" DOUBLE PRECISION NOT NULL,
    "unidadMedida" "UM_PRODUCTO" NOT NULL,
    "producto_id" INTEGER NOT NULL,
    "pedido_id" INTEGER NOT NULL,

    CONSTRAINT "detalle_pedidos_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "usuarios_id_key" ON "usuarios"("id");

-- CreateIndex
CREATE UNIQUE INDEX "usuarios_email_key" ON "usuarios"("email");

-- CreateIndex
CREATE UNIQUE INDEX "productos_id_key" ON "productos"("id");

-- CreateIndex
CREATE UNIQUE INDEX "pedidos_id_key" ON "pedidos"("id");

-- CreateIndex
CREATE UNIQUE INDEX "detalle_pedidos_id_key" ON "detalle_pedidos"("id");

-- AddForeignKey
ALTER TABLE "pedidos" ADD CONSTRAINT "pedidos_cliente_id_fkey" FOREIGN KEY ("cliente_id") REFERENCES "usuarios"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "detalle_pedidos" ADD CONSTRAINT "detalle_pedidos_producto_id_fkey" FOREIGN KEY ("producto_id") REFERENCES "productos"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "detalle_pedidos" ADD CONSTRAINT "detalle_pedidos_pedido_id_fkey" FOREIGN KEY ("pedido_id") REFERENCES "pedidos"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
