#include <stdio.h>
#include <SFML/Graphics.hpp>
#include <mpi.h>
#include <time.h>
using namespace sf;

int width = 400;
int height = 400;
int N_rectangle = 40;

struct complex {
	float real;
	float imag;
};


int cal_pixel(complex c) {
	int count = 0;
	int max = 256;
	complex z;
	z.real = 0;
	z.imag = 0;
	float temp, lengthsq;
	do {
		temp = z.real * z.real - z.imag * z.imag + c.real;
		z.imag = 2 * z.real * z.imag + c.imag;
		z.real = temp;
		lengthsq = z.real * z.real;
		count++;
	} while ((lengthsq < 4.0) && (count < max));
	return count;
}


clock_t starttime, endtime;
clock_t total_start_time, total_end_time;
int data[400][400];
int block[16002];
int temblock[16002];
int main(int argc, char** argv) {

	MPI_Init(&argc, &argv);
	int myid;
	int numprocs;
	MPI_Comm_rank(MPI_COMM_WORLD, &myid);
	MPI_Comm_size(MPI_COMM_WORLD, &numprocs);
	MPI_Status status;

	float minR = -2;
	float minI = -2;
	float maxR = 2;
	float maxI = 2;
	float scale_real, scale_imag;
	scale_real = (maxR - minR) / width;
	scale_imag = (maxI - minI) / height;
	complex c;
	int cl;
	if (myid == 0)
	{
		total_start_time = clock();
		int count = 0;
		int column = 0;
		int numblock = width / N_rectangle;
		int blocksize = N_rectangle * height;
		//멀티프로세서 일 때
		if (numprocs > 1) {
			for (int k = 1; k < numprocs && column < width; k++) {
				MPI_Send(&column, 1, MPI_INT, k, 1, MPI_COMM_WORLD);
				count++;
				column += N_rectangle;
			}
			int cur = 0;
			int k;
			int start, end;
			do {
				MPI_Recv(&temblock, 16002, MPI_INT, MPI_ANY_SOURCE, 0, MPI_COMM_WORLD, &status);
				//16001은 slave의 인덱스, 16000은 시작위치, 0~15999는 블록 데이터
				cur = temblock[16001];
				if (column < width) {
					MPI_Send(&column, 1, MPI_INT, cur, 1, MPI_COMM_WORLD);
					column += N_rectangle;

				}
				else {
					//모든 블락처리시 slave에게 종료신호를 보냄 종료조건은 coulmn==width
					count--;
					MPI_Send(&column, 1, MPI_INT, cur, 1, MPI_COMM_WORLD);
				}
				start = temblock[16000];
				end = start + N_rectangle;
				k = 0;
				//데이터배열에 저장
				for (int x = start; x < end; x++)
					for (int y = 0; y < height; y++) {
						data[y][x] = temblock[k];
						k++;
					}

			} while (count > 0);
		}
		//싱글프로세서 일 때 마스터 코어가 모든 연산을 함.
		else {
			starttime = clock();
			for (int b = 0; b < numblock;b++) {
				int s = b * N_rectangle;
				int e = s + N_rectangle;
				for (int x = s; x < e; x++)
				{
					c.real = minR + ((float)x * scale_real);
					for (int y = 0; y < height; y++) {
						c.imag = minI + ((float)y * scale_imag);
						cl = cal_pixel(c);
						data[y][x] = cl;

					}

				}
				endtime = clock();
				printf("process %d complete a Block, time: %fs\n", myid, (double)(endtime - starttime) / CLOCKS_PER_SEC);
				starttime = clock();
			}
		}
		total_end_time = clock();
		printf("\ntotal time in dynamic allocation:%fs\n\n", (double)(total_end_time - total_start_time) / CLOCKS_PER_SEC);


		RenderWindow window(VideoMode(width, height), "Mandlebrot set");
		Image image;
		image.create(width, height);
		Texture texture;
		Sprite sprite;
		while (window.isOpen()) {
			Event event;
			while (window.pollEvent(event))
			{
				if (event.type == Event::Closed) window.close();
			}
			for (int y = 0; y < height; y++)
				for (int x = 0; x < width; x++) {
					image.setPixel(x, y, Color(255 - data[y][x], 255 - data[y][x], 255 - data[y][x]));

				}

			window.clear();
			texture.loadFromImage(image);
			sprite.setTexture(texture);
			window.draw(sprite);
			window.display();
		}

	}
	//slave
	else {
		int start, end;
		int x, y, t;
		starttime = clock();
		MPI_Recv(&start, 1, MPI_INT, MPI_ANY_SOURCE, 1, MPI_COMM_WORLD, &status);

		while (start != width) { //종료조건 받은데이터가 column의 마지막좌표 일 때
			end = start + N_rectangle;
			t = 0;
			for (x = start; x < end; x++)
			{
				c.real = minR + ((float)x * scale_real);
				for (y = 0; y < width; y++) {
					c.imag = minI + ((float)y * scale_imag);
					block[t] = cal_pixel(c);
					t++;
				}
			}
			block[16000] = start;
			block[16001] = myid;
			// 0~15999는 데이터 16000은 블락시작위치 16001은 slave의 인덱스
			MPI_Send(&block, 16002, MPI_INT, 0, 0, MPI_COMM_WORLD);
			endtime = clock();
			printf("process %d complete a Block, time: %fs\n", myid, (double)(endtime - starttime) / CLOCKS_PER_SEC);
			starttime = clock();
			MPI_Recv(&start, 1, MPI_INT, MPI_ANY_SOURCE, 1, MPI_COMM_WORLD, &status);

		}
	}
	MPI_Finalize();
	return 0;
}