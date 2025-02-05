#include"SeqListFunc.h"
SeqList* InitList_Sq(int nSize) {
	SeqList* pSeqList;
	pSeqList = new SeqList;
	pSeqList->nLens = 0;
	pSeqList->nMax = nSize;
	pSeqList->pElem = new DataType[nSize];
	return pSeqList;
}