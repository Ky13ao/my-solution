// Lab 20-2 https://docs.google.com/document/d/1F0kRLQ5tII1jvUjBvoWFAWNUBXHfXRgeKdl5VJbRVy4/edit
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

#define NUM_ORDERS 11
#define NUM_WORKERS 6

typedef struct {
  int id;
  int workerid;
  int bCompleted;
}Order;

typedef struct {
  pthread_t thread;
  int status;
}worker_t;

typedef struct {
  int index;
  Order orders[NUM_ORDERS];
}PipelineData;

void pipelineMain();
void bossworkerMain();

void main(){
  // pipelineMain();
  bossworkerMain();
}

void *pipelineSoltn(void *);

void pipelineMain(){
  worker_t workers[NUM_WORKERS];
  for (int j = 0; j<NUM_WORKERS; j++){
    workers[j].status=-1;
  }
  PipelineData pipelineData;
  pipelineData.index = 0;
  for(int j = 0; j<NUM_ORDERS; j++){
    pipelineData.orders[j].id = j + 1;
    pipelineData.orders[j].bCompleted = 0;
  }
  
  for(int pipeId=0; pipeId<NUM_ORDERS; pipeId++){
    int freeWorkerIdx=-1;
    for (int j = 0; j<NUM_WORKERS; j++){
      if(workers[j].status==-1){
        freeWorkerIdx = j;
        break;
      }
    }
    while(freeWorkerIdx<0){
      for (int j = 0; j<pipeId; j++){
        if(pipelineData.orders[j].bCompleted==1){
          freeWorkerIdx=pipelineData.orders[j].workerid;
          pipelineData.orders[j].bCompleted=2;
          break;
        }
      }
    }
    pipelineData.orders[pipeId].workerid=freeWorkerIdx;
    workers[freeWorkerIdx].status=0;
    pthread_create(&workers[freeWorkerIdx].thread, NULL, pipelineSoltn, &pipelineData);
  }
  for(int j=0; j<NUM_WORKERS; j++){
    pthread_join(workers[j].thread, NULL);
  }
  // exit(0);
}

void *bossworkerSoltn(void *);

void bossworkerMain(){
  worker_t workers[NUM_WORKERS];
  for (int j = 0; j<NUM_WORKERS; j++){
    workers[j].status=-1;
  }
  Order orders[NUM_ORDERS];
  for(int orderId = 0; orderId<NUM_ORDERS; orderId++){
    int freeWorkerIdx = -1;
    // tìm worker rảnh
    for (int j = 1; j<NUM_WORKERS; j++){
      if(workers[j].status==-1){
        freeWorkerIdx = j;
        break;
      }
    }
    // nếu không có luồng rảnh đợi luồng hoàn thành
    while(freeWorkerIdx<0){
      for(int j = 0; j<=orderId; j++){
        if(orders[j].bCompleted==1){
          freeWorkerIdx = orders[j].workerid; 
          workers[freeWorkerIdx].status=-1;
          orders[j].bCompleted=2;
          break;
        }
      }
    }
    orders[orderId].id = orderId + 1;
    orders[orderId].bCompleted = 0;
    orders[orderId].workerid = freeWorkerIdx;
    pthread_create(&workers[freeWorkerIdx].thread, NULL, bossworkerSoltn, &orders[orderId]);
    workers[freeWorkerIdx].status=0;
  }
  for(int j=1; j<NUM_WORKERS; j++){
    pthread_join(workers[j].thread, NULL);
  }
  // exit(0);
}

void *obtainOrder(void *);
void *analyzeOrder(void *);
void *cutWood(void *);
void *paintNDecorate(void *);
void *assemble(void *);
void *deliver(void *);

void *bossworkerSoltn(void *order_){
  Order *order = (Order*)order_;
  int orderId = order->id;
  obtainOrder(&orderId);
  analyzeOrder(&orderId);
  cutWood(&orderId);
  paintNDecorate(&orderId);
  assemble(&orderId);
  deliver(&orderId);
  printf("Order %d: Completed by Worker%d. BW\n", orderId, order->workerid);
  order->bCompleted = 1;
  return NULL;
}

void *pipelineSoltn(void *data){
  PipelineData *pipelineData = (PipelineData*)data;
  int pipeId = pipelineData->index;
  pipelineData->index++;
  int orderId = pipelineData->orders[pipeId].id;
  obtainOrder(&orderId);
  analyzeOrder(&orderId);
  cutWood(&orderId);
  paintNDecorate(&orderId);
  assemble(&orderId);
  deliver(&orderId);
  printf("Order %d: Completed by Worker%d. Pipe\n", orderId, pipelineData->orders[pipeId].workerid);
  pipelineData->orders[pipeId].bCompleted=1;
  return NULL;
}

void *obtainOrder(void *order){
  usleep(20000);
  printf("Order %d: Order obtained.\n", *(int*)order);
  return NULL;
}

void *analyzeOrder(void *order){
  usleep(20000);
  printf("Order %d: Order analysis completed.\n", *(int*)order);
  return NULL;
}

void *cutWood(void *order){
  usleep(20000);
  printf("Order %d: Wood cutting completed.\n", *(int*)order);
  return NULL;
}

void *paintNDecorate(void *order){
  usleep(20000);
  printf("Order %d: Painting and decorating completed.\n", *(int*)order);
  return NULL;
}

void *assemble(void *order){
  usleep(20000);
  printf("Order %d: Assembly completed.\n", *(int*)order);
  return NULL;
}


void *deliver(void *order){
  usleep(20000);
  printf("Order %d: Delivery completed.\n", *(int*)order);
  return NULL;
}

