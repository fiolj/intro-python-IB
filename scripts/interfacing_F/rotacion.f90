module rotaciones

contains
  !> matrix_rotation
  !! Crea la matriz de rotación correspondiente a los tres ángulos de Euler
  !! 
  !! @param angles 
  !! @return R
  function matrix_rotation(angles) result(R)
    implicit none
    real(8), dimension(3), intent(IN) :: angles
    real(8), dimension(3,3) :: R
    real(8) :: cx, cy, cz, sx, sy, sz

    cx = cos(angles(1)); cy = cos(angles(2)); cz = cos(angles(3))
    sx = sin(angles(1)); sy = sin(angles(2)); sz = sin(angles(3))

    R(1,1) = cx*cz - sx*cy*sz
    R(1,2) = cx*sz + sx*cy*cz
    R(1,3) = sx*sy

    R(2,1) = -sx*cz - cx*cy*sz
    R(2,2) = -sx*sz + cx*cy*cz
    R(2,3) = cx*sy

    R(3,1) = sy*sz
    R(3,2) = -sy*cz
    R(3,3) = cy
  end function matrix_rotation

  !> rotate
  !!
  !! @param angles 
  !! @param v 
  !! @param N longitud del vector v 
  !! @return y
  function rotate(angles, v, N) result(y)
    implicit none
    integer, intent(IN) :: N
    real(8), dimension(3), intent(IN) :: angles
    real(8), dimension(3,N), intent(IN) :: v
    real(8), dimension(3,N) :: y

    y = matmul(matrix_rotation(angles), v)
  end function rotate

end module rotaciones

program test_rotation
  USE rotaciones !, only: rotate
  implicit none
  integer, parameter :: Ndim=1000
  real(8), dimension(3) :: angle
  real(8), dimension(3, Ndim) :: v, y

  integer :: n, Nloops,i,j
  real(8) :: time_begin, time_end

  real(8), dimension(3, 3) :: R


  ! Selecciono Ndim vectores tridimensionales al azar
  call RANDOM_NUMBER(v)
  Nloops = 10000

  CALL CPU_TIME ( time_begin )
  do n=1,Nloops
    call RANDOM_NUMBER(angle)
    y= rotate(angle, v, Ndim)
  end do
  CALL CPU_TIME ( time_end )

  write (*,'(A,1PE12.2,A)') '# Tiempo usado:', (time_end - time_begin)/(1.e-3*Nloops), ' milisegundos por 1000 rotaciones'

  ! Test a simple case

  ! angle(1) = 1.0
  ! angle(2) = 2.0
  ! angle(3) = 3.0

  ! R = matrix_rotation(angle)
  ! ! do i=1,3
  ! !  write(*,'(3F8.3)') R(i,1),R(i,2),R(i,3)    
  ! ! end do

  ! do j=0,4
  !     v(1,j+1) = j*3+0
  !     v(2,j+1) = j*3+1
  !     v(3,j+1) = j*3+2
  ! end do
  ! y= rotate(angle, v, 5)

  ! do i=1,5
  !   write(*,'(3F8.3)') y(1,i),y(2,i),y(3,i)    
  ! end do

end program test_rotation
