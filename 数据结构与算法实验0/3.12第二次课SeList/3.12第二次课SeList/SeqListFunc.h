#pragma once
typedef int DataType;
struct SeqList
{
	int nLens;
	int nMax;
	DataType* pElem;
};
SeqList* InitList_Sq(int nSize);