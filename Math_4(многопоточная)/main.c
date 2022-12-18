#include <stdio.h>
#include <malloc.h>
#include <math.h>
#include <pthread.h>
#include <stdlib.h>
#include <time.h>

#define E 2.7182818284590452353602874713527

#define APPROXIMATION_THREADS_COUNT 2
#define DIFFERENCE_THREADS_COUNT 4

const double a = 10, n = 1000000, h = 2 * a / n;
int middle = n / 2;
double* x_array;
double* y_array;
double* discrepancy_array;

typedef struct Approximation {
    int sgn;
} Approximation;

typedef struct Difference {
    int sgn;
    int start;
    int end;
} Difference;

double count(int sgn, double y) {
    return (1 - sgn * h) * y;
}

void printResult() {
    for (int i = 0; i < n + 1; i++) {
        printf("%d x = %lf, y = %lf, discrepancy = %lf\n",
               i, x_array[i], y_array[i], discrepancy_array[i]);
    }
}

void* approximation(void *data) {
    Approximation *local_data = (Approximation *) data;
    int sgn = local_data->sgn;

    double y_cur = -1;
    double x_cur = 0;

    for (int i = 1; i < middle + 1; i++) {
        y_cur = count(sgn, y_cur);
        x_cur += sgn * h;
        x_array[middle + sgn * i] = x_cur;
        y_array[middle + sgn * i] = y_cur;
    }
    return EXIT_SUCCESS;
}

void countApproximation() {
    pthread_t thread[APPROXIMATION_THREADS_COUNT];
    Approximation *data = (Approximation *) malloc(sizeof(Approximation) * APPROXIMATION_THREADS_COUNT);

    y_array[middle] = -1;
    x_array[middle] = 0;

    for (int i = 0; i < APPROXIMATION_THREADS_COUNT; i++) {
        data[i].sgn = (i < APPROXIMATION_THREADS_COUNT / 2) ? -1 : 1;
        pthread_create(&thread[i], NULL, approximation, &data[i]);
    }

    for (int i = 0; i < APPROXIMATION_THREADS_COUNT; i++) {
        pthread_join(thread[i], NULL);
    }
}

void* discrepancy(void* data) {
    Difference *local_data = (Difference*) data;
    int sgn = local_data->sgn;
    int start = local_data->start;
    int end = local_data->end;

    for (int i = start; i < end; i++) {
        discrepancy_array[i] = -sgn * h * (-pow(E, -x_array[i])) * x_array[i] / 2;
    }
    return EXIT_SUCCESS;
}


void findDiscrepancy() {
    pthread_t thread[DIFFERENCE_THREADS_COUNT];
    Difference *data = (Difference*)malloc(sizeof(Difference) * DIFFERENCE_THREADS_COUNT);

    for (int i = 0; i < DIFFERENCE_THREADS_COUNT; i++) {
        data[i].sgn = (i < DIFFERENCE_THREADS_COUNT / 2) ? 1 : -1;
        data[i].start = i * (n / DIFFERENCE_THREADS_COUNT);
        data[i].end = (i + 1) * n / DIFFERENCE_THREADS_COUNT + 1;

        pthread_create(&thread[i], NULL, discrepancy, &data[i]);
    }

    for (int i = 0; i < DIFFERENCE_THREADS_COUNT; i++) {
        pthread_join(thread[i], NULL);
    }
}


int main() {
    x_array = (double*) malloc(sizeof(double) * (n + 1));
    y_array = (double*) malloc(sizeof(double) * (n + 1));
    discrepancy_array = (double *) malloc(sizeof(double) * (n + 1));

    clock_t time = clock();
    countApproximation();
    time = clock() - time;
    printf("Approximation time %lf sec\n",
            ((double)time) / CLOCKS_PER_SEC);


    time = clock();
    findDiscrepancy();
    time = clock() - time;
    printf("Count discrepancy time %lf sec\n",
            ((double)time) / CLOCKS_PER_SEC);

//    printResult();

    free(x_array);
    free(y_array);
    free(discrepancy_array);
    return 0;
}