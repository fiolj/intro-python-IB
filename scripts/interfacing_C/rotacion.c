#include<stdio.h>
#include<stdlib.h>
#include<math.h> 


    typedef struct {
      float m[3][3];
    } m3x3;

    typedef struct {
      float a[3];
    } v3;

  // !> matrix_rotation
  // !! Crea la matriz de rotación correspondiente a los tres ángulos de Euler
  // !! 
  // !! @param angles 
  // !! @return R

    m3x3 matrix_rotation(float angles[3]){

        m3x3 R;

        float cx = cos(angles[0]); 
        float cy = cos(angles[1]); 
        float cz = cos(angles[2]);
        float sx = sin(angles[0]); 
        float sy = sin(angles[1]); 
        float sz = sin(angles[2]);


        R.m[0][0] = cx*cz - sx*cy*sz;
        R.m[0][1] = cx*sz + sx*cy*cz;
        R.m[0][2] = sx*sy;

        R.m[1][0] = -sx*cz - cx*cy*sz;
        R.m[1][1] = -sx*sz + cx*cy*cz;
        R.m[1][2] = cx*sy;

        R.m[2][0] = sy*sz;
        R.m[2][1] = -sy*cz;
        R.m[2][2] = cy;

        return R;
  }

  v3 matmul3(m3x3 A, float b[3]){

      static v3 a;

      for(int i=0; i < 3; i++){
            a.a[0] = A.m[0][0] * b[0] + A.m[0][1] * b[1] + A.m[0][2] * b[2];
            a.a[1] = A.m[1][0] * b[0] + A.m[1][1] * b[1] + A.m[1][2] * b[2];
            a.a[2] = A.m[2][0] * b[0] + A.m[2][1] * b[1] + A.m[2][2] * b[2];
          }
    //  printf("%6.3f %6.3f %6.3f \n",a[0],a[1],a[2]);

      return a;
  }



    float * rotate(float angles[3], float *v, int N){
        
        m3x3 R = matrix_rotation(angles);
        

        float* y = (float*)malloc(3*N*sizeof(float));
        v3 p;

        printf("%p\n",y);
        for(int i=0; i<N; i++){
            // p = &y[i*3];
            p = matmul3(R,&v[i*3]);
            y[i*3+0] = p.a[0];
            y[i*3+1] = p.a[1];
            y[i*3+2] = p.a[2];
            // printf("%6.3f %6.3f %6.3f \n",y[i*3+0],y[i*3+1],y[i*3+2]);
        }
        return y;


  }


int main(){

  float angle[3] = { 0.0f, 0.0f, 3.141592f/2.0f};

  m3x3 R;

  int NDIM = 2;
  float* v = (float*)malloc(3*NDIM*sizeof(float));

  float *y;

  for (size_t j = 0; j < NDIM; j++)
      {
            v[j*3+0] = (j*3+0)*1.0f;
            v[j*3+1] = (j*3+1)*1.0f;
            v[j*3+2] = (j*3+2)*1.0f;
      }

  v[0] = (1)*1.0f;
  v[1] = (0)*1.0f;
  v[2] = (0)*1.0f;
  v[3] = (0)*1.0f;
  v[4] = (1)*1.0f;  
  v[5] = (0)*1.0f;



  R = matrix_rotation(angle);

    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            printf("%6.3f",R.m[i][j]);
            printf("   ");
        }
        printf("\n");
    }

  y = rotate(angle,v,NDIM);
  printf("%6.3f %6.3f %6.3f \n",y[0],y[1],y[2]);
  printf("%6.3f %6.3f %6.3f \n",y[3],y[4],y[5]);
  // for (size_t i = 0; i < NDIM; i++)
  // {
  //    printf("%6.3f %6.3f %6.3f \n",y[i*3],y[i*3+1],y[i*3+2]);
  // }
  

}  
