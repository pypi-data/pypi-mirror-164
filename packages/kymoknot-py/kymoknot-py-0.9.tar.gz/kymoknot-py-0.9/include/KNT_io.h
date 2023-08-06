/********************************************************
 * LT 02/03/2011                                        *
 *                                                      *
 * Input / Output function for KNT_arc structures.      *
 *                                                      *
 * KNOWN BUGS:                                          *
 *                                                      *
 * KNTIOread_ function may fail if input file malformed *
 *                                                      *
 ********************************************************/

#ifndef HDR_KNTIO
#define HDR_KNTIO

#define  _GNU_SOURCE

#include "KNT_arc.h"
#include <stdio.h>
#include <sys/types.h>

//#include "KNT_defaults.h"

/* define linked list structure for objects names in hdf5 file */
/*--load data from file---------------------*/
KNTarc *KNTIOread_ring(FILE *);
KNTarc *KNTIOread_linear(FILE *);
void KNTIOprint_arc(FILE *out, KNTarc *knt_ptr, int start, int end);
void KNTIOprint_ring(FILE *out, KNTarc *knt_ptr);
void KNTIOprint_linear(FILE *out, KNTarc *knt_ptr);


//Helpers for python bindings
KNTarc *KNTIO_mat_to_arc_linear(double *mat, int length);
KNTarc *KNTIO_mat_to_arc_ring(double *mat, int length);

#endif /* HDR_KNTIO */
