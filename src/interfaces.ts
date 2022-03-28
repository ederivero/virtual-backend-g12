export interface ICreateMovimiento {
  monto: number
  tipo: 'INGRESO' | 'EGRESO'
  descripcion?: string
  moneda: 'SOLES' | 'DOLARES' | 'EUROS'
  fecha_creacion?: Date
  categoria: number
}
export interface IGetMovimiento extends ICreateMovimiento {
  id: string
}

export interface IParams {
  tipo?: 'INGRESO' | 'EGRESO'
  categoria?: number
}

export interface IResponse<I> {
  message: string
  content: Array<I>
}

export interface ILogin {
  correo: string
  password: string
}

export interface IRegister extends ILogin {
  nombre: string
  apellido: string
}
