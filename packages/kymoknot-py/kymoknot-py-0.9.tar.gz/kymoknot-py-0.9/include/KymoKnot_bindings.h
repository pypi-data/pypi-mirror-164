#ifndef KymoKnot_Bindings_H
#define KymoKnot_Bindings_H


#include "KNT_searches.h"

#define MEMLEN 1000

//
//##########################################
//Search
//##########################################
//

//
//Search input structs
//

//parameters to configure a knot search from python
//these parameters are common for all searches
typedef struct search_config {

    int f_arc_start;
    int arc_start;

    int f_arc_end;
    int arc_end;

    //char fname_prev_search[1024];
    //int f_prev_search;
    //

    char * chain_file_path;

    int max_stride;
    int f_max_stride;
    int _min_stride;
    int _simp_sweeps;

    int search_type[N_SEARCHES];

    int memlen;

    int print_conf;

    char closure_type[CL_STR_MAXLEN];
    char close_subchain[CL_STR_MAXLEN];

    int seed;

} search_config_t;


//parameters to really perform a knot search,
//including chain data and start/stop positions
//
//if start/stop are set to -1, values are taken from:
// - search_config.arc_start
// - search_config.arc_end
//
typedef struct search_data_entry {

    double *mat;

    //number of 3d coordinates
    //real size of the area pointed by mat
    //is 3 * len * sizeof(double) [bytes]
    int len;

    int arc_start;
    int arc_end;
} search_data_entry_t;


//
//Search output structs
//

//structure received from python that contains data for searches
typedef struct search_data {
    int len;
    search_data_entry_t **entries;
} search_data_t;


typedef struct knt_entry {

    int idx;
    char knot_ids[IDS_MAXLEN];

    //
    //field reporting the kind of search
    //that returned this knot
    //
    //used for differentiate between knots
    //where *_t2 fields have a meaning (beacuse a result of a tangle
    //search) and nodes where *_t2 fields are meaningless.
    //
    int search_type;

    int start;
    int end;

    int start_t2; // for tangles
    int end_t2;   // for tangles

    int length;

} knt_entry_t;


//all knots found on a chain
typedef struct search_retval_entry {
    size_t len;
    knt_entry_t *entries;
} search_retval_entry_t;


//
//the structure that contains the search results
//for each chain, for all searches
typedef struct search_retval_llnode {
    search_retval_entry_t * sres[4];
    struct search_retval_llnode * next;
} search_retval_llnode_t;


//a linked list of search_retval_llnode_t
typedef struct search_retval_ll {

    int len;
    search_retval_llnode_t * head;
    search_retval_llnode_t * tail;

} search_retval_ll_t;


search_retval_ll_t * srlist_init();
int srlist_push(search_retval_ll_t *list, search_retval_llnode_t * el);
search_retval_llnode_t * srnode_init();


//search functions
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


//
//############################################
//Close
//############################################
//


//calling search_data_t as close_data_t,
//they are basically the same, extra attributes
//like start or end are ignored
typedef search_data_t close_data_t;


typedef struct close_retval_entry {
    size_t len;
    double *coord;
} close_retval_entry_t;


typedef struct close_retval {
    size_t len;
    close_retval_entry_t *entries;
} close_retval_t;


//close functions
close_retval_t *init_close_retval(size_t len);

close_retval_t *KymoKnot_close(close_data_t *c_data);

void free_close_retval(close_retval_t *clretval);

#endif
