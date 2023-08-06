# 1 "include/KymoKnot_bindings.h"
# 1 "<built-in>" 1
# 1 "<built-in>" 3
# 366 "<built-in>" 3
# 1 "<command line>" 1
# 1 "<built-in>" 2
# 1 "include/KymoKnot_bindings.h" 2




# 1 "include/KNT_searches.h" 1
# 6 "include/KymoKnot_bindings.h" 2
# 21 "include/KymoKnot_bindings.h"
typedef struct search_config {

    int f_arc_start;
    int arc_start;

    int f_arc_end;
    int arc_end;





    char * chain_file_path;

    int max_stride;
    int f_max_stride;
    int _min_stride;
    int _simp_sweeps;

    int search_type[4];

    int memlen;

    int print_conf;

    char closure_type[64];
    char close_subchain[64];

    int seed;

} search_config_t;
# 61 "include/KymoKnot_bindings.h"
typedef struct search_data_entry {

    double *mat;




    int len;

    int arc_start;
    int arc_end;
} search_data_entry_t;







typedef struct search_data {
    int len;
    search_data_entry_t **entries;
} search_data_t;


typedef struct knt_entry {

    int idx;
    char knot_ids[128];
# 99 "include/KymoKnot_bindings.h"
    int search_type;

    int start;
    int end;

    int start_t2;
    int end_t2;

    int length;

} knt_entry_t;



typedef struct search_retval_entry {
    size_t len;
    knt_entry_t *entries;
} search_retval_entry_t;





typedef struct search_retval_llnode {
    search_retval_entry_t * sres[4];
    struct search_retval_llnode * next;
} search_retval_llnode_t;



typedef struct search_retval_ll {

    int len;
    search_retval_llnode_t * head;
    search_retval_llnode_t * tail;

} search_retval_ll_t;


search_retval_ll_t * srlist_init();
int srlist_push(search_retval_ll_t *list, search_retval_llnode_t * el);
search_retval_llnode_t * srnode_init();



void init_search_config(search_config_t *param);

search_retval_ll_t *KymoKnot_linear(
        search_config_t *s_config,
        search_data_t *s_data
);

search_retval_ll_t *KymoKnot_linear_file(
        search_config_t *s_config
);

search_retval_ll_t *KymoKnot_ring_file(
        search_config_t *s_config
);

search_retval_ll_t *KymoKnot_ring(
        search_config_t *s_config,
        search_data_t *s_data
);

void free_search_retval(search_retval_ll_t *search_results);
# 177 "include/KymoKnot_bindings.h"
typedef search_data_t close_data_t;


typedef struct close_retval_entry {
    size_t len;
    double *coord;
} close_retval_entry_t;


typedef struct close_retval {
    size_t len;
    close_retval_entry_t *entries;
} close_retval_t;



close_retval_t *init_close_retval(size_t len);

close_retval_t *KymoKnot_close(close_data_t *c_data);

void free_close_retval(close_retval_t *clretval);
