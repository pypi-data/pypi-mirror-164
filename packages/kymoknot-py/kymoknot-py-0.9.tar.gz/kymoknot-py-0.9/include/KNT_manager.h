#ifndef __H_MANAGER
#define __H_MANAGER

#define _VERSION_ "1.6"
#define MEMLEN 1000

#include "KNT_defaults.h"
#include "KNT_arc.h"
#include "KNT_lib.h"

#define  _GNU_SOURCE

#include <stdio.h>
#include <stdlib.h>
#include "KNT_searches.h"

#include "KymoKnot_bindings.h"

//
//defining a new type close_subchain which is a function pointer
//just syntactic sugar for readability.
//see:
//https://stackoverflow.com/questions/4295432/typedef-function-pointer
//
typedef KNTarc (*close_subchain)(KNTarc *, int, int);


//as above
typedef void (*LocFnc)(
        KNTarc *knt_ptr,
        KNTarc *knt_rect,
        int st_p,
        int end_p,
        close_subchain cls,
        KNTID_wspace *ws
);


typedef struct _SearchManager_t {
    int st_p;
    int end_p;
    int S;
    close_subchain close_subchain_ptr;
    LocFnc LocFnc_ptr;
    char arc_id;
    char fout_prefix[16];
    char fout_expl[1024];
    char fout_hdr[512];
    FILE *fout;
} searchManager_t;


struct param_t {
    // "private"
    int _min_stride;
    int _simp_sweeps;
    // "public" (can be modified by command line arguments)
    char filename[1024];
    char fname_prev_search[1024];
    FILE *fin;
    FILE *fin_prev_search;
    int memlen;
    unsigned int seed;
    int max_stride;
    int arc_start;
    int arc_end;
    int print_conf;
    char closure_type;
    int search_type[N_SEARCHES];
    searchManager_t search[N_SEARCHES];
    // non-optional
    int counter;
    KNTID_wspace *kntid_ws;
    //flags
    int f_arc_start, f_arc_end, f_prev_search, f_max_stride;
};

void set_default_behaviour(struct param_t *param);

void read_command_line(struct param_t *param, int argc, char **argv);

void set_search_params(struct param_t *param, search_config_t *cl_params);
void set_search_brackets_linear(struct param_t *param, int cnt, int arc_len);

void set_search_brackets_ring(struct param_t *param, int cnt, int arc_len);

void settings2string(char *string, struct param_t *param);

void settings2stderr(char *string, struct param_t *param);

void searchManagers_init(struct param_t *param, char *settingsString);

void print_search_results_linear(KNTarc *knt_ptr, searchManager_t *sM, int cnt, struct param_t *param);

void print_search_results_ring(KNTarc *knt_ptr, searchManager_t *sM, int cnt, struct param_t *param);

int get_idx_rect_chain(KNTarc *knt_rect, int idx_orig);

void kymoknot_initialize_cli(struct param_t *param, int argc, char **argv);

void kymoknot_initialize_python(struct param_t *param, search_config_t *cl_params);
void kymoknot_terminate(struct param_t *param);

void print_help();

close_subchain str_to_closure_func(char *str, size_t maxlen);

void init_search_params(search_config_t *param);

search_retval_entry_t *init_search_results(int res_nr);

search_retval_entry_t *report_search_results(
        KNTarc *knt_ptr,
        int search_type,
        int cnt,
        struct param_t *param
);


void free_retval_entry(search_retval_entry_t *report);
#endif //__H_MANAGER
