#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <getopt.h>
#include <unistd.h>
#include <time.h>
#include "KNT_defaults.h"
#include "KNT_arc.h"
#include "KNT_lib.h"
#include "KNT_closures.h"
#include "KNT_io.h"
#include "KNT_qhull.h"
#include "KNT_simplify.h"
#include "KNT_manager.h"
#include "my_memory.h"

#include "KymoKnot_bindings.h"


void init_search_config(search_config_t *param) {

    param->f_arc_start = FALSE;
    param->arc_start = DONT_CARE;

    param->f_arc_end = FALSE;
    param->arc_end = DONT_CARE;

    //param->fname_prev_search[0] = NULL;
    //param->f_prev_search        = FALSE;
    //
    param->chain_file_path = NULL;

    param->max_stride = 0;
    param->f_max_stride = FALSE;
    param->_min_stride = 2;
    param->_simp_sweeps = 4;

    param->search_type[BU] = TRUE;
    param->search_type[TD] = FALSE;
    param->search_type[UNS] = FALSE;
    param->search_type[TNG] = FALSE;

    param->memlen = MEMLEN;
    param->print_conf = FALSE;

    strncpy(param->closure_type, CL_QHULLHYB, STR_OUT_MAXLEN);
    strncpy(param->close_subchain, CL_QHULLHYB, STR_OUT_MAXLEN);

    param->seed = time(NULL) + getpid();

}


search_retval_ll_t * srlist_init() {

    search_retval_ll_t * res;

    res = malloc(sizeof(*res));

    res->len = 0;
    res->head = NULL;
    res->tail = NULL;

    return res;
}


int srlist_push(search_retval_ll_t *list, search_retval_llnode_t * el) {

    el->next = NULL;

    if (list->head == NULL && list->tail == NULL) {
        list->head = el;
        list->tail = el;
    }
    else {
        list->tail->next = el;
        list->tail = el;
    }

    list->len++;

    return 0;
}


search_retval_llnode_t * srnode_init() {

    search_retval_llnode_t * res;
    int i;

    res = malloc(sizeof(*res));
    for(i=0; i<N_SEARCHES; i++) {
        res->sres[i] = NULL;
    }
    res->next = NULL;
    return res;
}


search_retval_ll_t * KymoKnot_linear_file(
        search_config_t *s_config
) {
    int i;

    KNTid knot_type;    // knot identifier. See KNT_identify.h, KNT_table.h
    KNTarc closed_arc;
    KNTarc *knt_rect;
    KNTarc *arc_ptr;

    search_retval_ll_t * res;
    res = srlist_init();

    struct param_t param;
    kymoknot_initialize_python(&param, s_config);

    //printf("Performing search: %s\n", s_config->closure_type);

    close_subchain closure_func;
    closure_func = str_to_closure_func(s_config->closure_type, CL_STR_MAXLEN);

    while ((arc_ptr = KNTIOread_linear(param.fin)) != NULL) {

        if (arc_ptr == NULL) {
            failed("Cannot allocate memory for arc_linear");
        }

        search_retval_llnode_t *  cnode = srnode_init();

        set_search_brackets_linear(&param, param.counter, arc_ptr->len);
        //allocate qhull working space
        qhull_init(3 * (arc_ptr->len + MAX_CLS_POINTS));

        //close chain and rotate it
        closed_arc = closure_func(arc_ptr, param.arc_start, param.arc_end);

        KNTLcentre_rotate_random(&closed_arc);
        //--rectification (excluding first and last bead)
        int start_local = 0;
        int end_local = param.arc_end - param.arc_start;
        if (param.f_max_stride == FALSE) {
            param.max_stride = arc_ptr->len / 50;
        }
        knt_rect = KNTLrectify_coord_local(
                &closed_arc, start_local,
                end_local,
                param._min_stride,
                param.max_stride
        );
        fprintf(stderr, "closed_arc.len %d -- knt_rect->len %d\n", closed_arc.len, knt_rect->len);
        //--compute knot type of closed portion
        knot_type = KNTID_identify_knot(knt_rect, param.kntid_ws);
        closed_arc.knot_type = knt_rect->knot_type;
        //--bracketing on rectified chain
        int start = get_idx_rect_chain(knt_rect, start_local);
        int end = get_idx_rect_chain(knt_rect, end_local);

        //--Begin the search

        for (int j = 0; j < N_SEARCHES; j++) {

            if (param.search_type[j]) {

                if (param.f_arc_start || param.f_arc_end) {
                    param.search[j].st_p = start;
                    param.search[j].end_p = end;
                } else {
                    param.search[j].st_p = DONT_CARE;
                    param.search[j].end_p = DONT_CARE;
                }
                param.search[j].S = param.max_stride;
                param.search[j].fout = NULL;

                if (knot_type.k_id == K_Un) {

                    search_retval_entry_t *curr;

                    curr = init_search_results(1);
                    cnode->sres[j] = curr;

                    knt_entry_t *entry = &curr->entries[0];
                    entry->knot_ids[0] = 0;
                    entry->idx = param.counter;

                    entry->search_type = j;

                    entry->start = -1;
                    entry->end = -1;

                    entry->start_t2 = -1;
                    entry->end_t2 = -1;

                    entry->length = -1;

                    //writes knot_ids inside entry
                    KNTID_print_knot(entry->knot_ids, IDS_MAXLEN, knot_type);
                } else {

                    param.search[j].LocFnc_ptr(
                            &closed_arc,
                            knt_rect,
                            param.search[j].st_p,
                            param.search[j].end_p,
                            param.search[j].close_subchain_ptr,
                            param.kntid_ws
                    );

                    cnode->sres[j] = report_search_results(
                            &closed_arc,
                            j,
                            param.counter,
                            &param
                    );
                }

                //printf("res report: %p\n\n", res->entries[i]);
            }
        }

        srlist_push(res, cnode);

        KNTfree_arc(&closed_arc);
        KNTfree_arc(arc_ptr);
        KNTfree_arc(knt_rect);
        qhull_terminate();
        param.counter++;
    }

    kymoknot_terminate(&param);
    return res;
}


search_retval_ll_t *KymoKnot_ring_file(
        search_config_t *s_config
) {
    int i;

    KNTid knot_type;  // knot identifier. See KNT_identify.h, KNT_table.h
    KNTarc *knt_rect;
    KNTarc *knt_ptr;

    search_retval_ll_t *res;
    res = srlist_init();

    struct param_t param;
    kymoknot_initialize_python(&param, s_config);

    while ((knt_ptr = KNTIOread_ring(param.fin)) != NULL) {

        if (knt_ptr == NULL) {
            failed("Cannot allocate memory for arc_ring");
        }

        search_retval_llnode_t *  cnode = srnode_init();

        set_search_brackets_ring(&param, param.counter, knt_ptr->len);
        //allocate qhull working space
        qhull_init(3 * (knt_ptr->len + MAX_CLS_POINTS));
        //close chain and rotate it
        KNTLcentre_rotate_random(knt_ptr);
        //--rectification (excluding first and last bead)
        int start_local;
        int end_local;
        //XXX this condition needs to be improved
        if (param.f_arc_start || param.f_arc_end) {
            start_local = param.arc_start;
            end_local = param.arc_end;
        } else {
            start_local = 0;
            end_local = knt_ptr->len - 1;
            param.arc_start = start_local;
            param.arc_end = end_local;
        }

        if (param.f_max_stride == FALSE) {
            param.max_stride = knt_ptr->len / 50;
        }
        knt_rect = KNTLrectify_coord_local(knt_ptr, start_local, end_local, param._min_stride, param.max_stride);
        int start = get_idx_rect_chain(knt_rect, start_local);
        int end = get_idx_rect_chain(knt_rect, end_local);
        //
        fprintf(stderr, "knt_ptr->len %d -- knt_rect->len %d\n", knt_ptr->len, knt_rect->len);
        //--compute knot type of closed portion
        knot_type = KNTID_identify_knot(knt_rect, param.kntid_ws);
        knt_ptr->knot_type = knt_rect->knot_type;
        //--bracketing on rectified chain
        //--Begin the search
        for (int j = 0; j < N_SEARCHES; j++) {

            if (param.search_type[j]) {

                if (param.f_arc_start || param.f_arc_end) {
                    param.search[j].st_p = start;
                    param.search[j].end_p = end;
                } else {
                    param.search[j].st_p = DONT_CARE;
                    param.search[j].end_p = DONT_CARE;
                }
                param.search[j].S = param.max_stride;
                param.search[j].fout = NULL;

                if (knot_type.k_id == K_Un) {

                    search_retval_entry_t *curr;

                    curr = init_search_results(1);
                    cnode->sres[j] = curr;

                    knt_entry_t *entry = &curr->entries[0];
                    entry->knot_ids[0] = 0;
                    entry->idx = param.counter;

                    entry->search_type = j;

                    entry->start = -1;
                    entry->end = -1;

                    entry->start_t2 = -1;
                    entry->end_t2 = -1;

                    entry->length = -1;

                    //writes knot_ids inside entry
                    KNTID_print_knot(entry->knot_ids, IDS_MAXLEN, knot_type);

                } else {

                    param.search[j].LocFnc_ptr(
                            knt_ptr,
                            knt_rect,
                            param.search[j].st_p,
                            param.search[j].end_p,
                            param.search[j].close_subchain_ptr,
                            param.kntid_ws
                    );

                    cnode->sres[j] = report_search_results(
                            knt_ptr,
                            j,
                            param.counter,
                            &param
                    );

                }

                //printf("res report: %p\n\n", res->entries[i]);
            }
        }

        srlist_push(res, cnode);

        KNTfree_arc(knt_ptr);
        KNTfree_arc(knt_rect);
        qhull_terminate();
        param.counter++;
    }
    kymoknot_terminate(&param);

    return res;
}


search_retval_ll_t * KymoKnot_linear(
        search_config_t *s_config,
        search_data_t *s_data
) {
    int i;

    KNTid knot_type;    // knot identifier. See KNT_identify.h, KNT_table.h
    KNTarc closed_arc;
    KNTarc *knt_rect;
    KNTarc *arc_ptr;
    search_data_entry_t *ent;

    search_retval_ll_t *res;
    res = srlist_init();

    struct param_t param;
    kymoknot_initialize_python(&param, s_config);

    //printf("Performing search: %s\n", s_config->closure_type);

    close_subchain closure_func;
    closure_func = str_to_closure_func(s_config->closure_type, CL_STR_MAXLEN);

    for (i = 0; i < s_data->len; i++) {

        search_retval_llnode_t *  cnode = srnode_init();

        ent = s_data->entries[i];
        arc_ptr = KNTIO_mat_to_arc_linear(ent->mat, ent->len);

        if (arc_ptr == NULL) {
            failed("Cannot allocate memory for arc_linear");
        }

        set_search_brackets_linear(&param, param.counter, arc_ptr->len);
        //allocate qhull working space
        qhull_init(3 * (arc_ptr->len + MAX_CLS_POINTS));

        //close chain and rotate it
        closed_arc = closure_func(arc_ptr, param.arc_start, param.arc_end);

        KNTLcentre_rotate_random(&closed_arc);
        //--rectification (excluding first and last bead)
        int start_local = 0;
        int end_local = param.arc_end - param.arc_start;
        if (param.f_max_stride == FALSE) {
            param.max_stride = arc_ptr->len / 50;
        }
        knt_rect = KNTLrectify_coord_local(
                &closed_arc, start_local,
                end_local,
                param._min_stride,
                param.max_stride
        );
        fprintf(stderr, "closed_arc.len %d -- knt_rect->len %d\n", closed_arc.len, knt_rect->len);
        //--compute knot type of closed portion
        knot_type = KNTID_identify_knot(knt_rect, param.kntid_ws);
        closed_arc.knot_type = knt_rect->knot_type;
        //--bracketing on rectified chain
        int start = get_idx_rect_chain(knt_rect, start_local);
        int end = get_idx_rect_chain(knt_rect, end_local);

        //--Begin the search
        for (int j = 0; j < N_SEARCHES; j++) {

            if (param.search_type[j]) {

                if (param.f_arc_start || param.f_arc_end) {
                    param.search[j].st_p = start;
                    param.search[j].end_p = end;
                } else {
                    param.search[j].st_p = DONT_CARE;
                    param.search[j].end_p = DONT_CARE;
                }
                param.search[j].S = param.max_stride;
                param.search[j].fout = NULL;

                if (knot_type.k_id == K_Un) {

                    search_retval_entry_t *curr;

                    curr = init_search_results(1);
                    cnode->sres[j] = curr;

                    knt_entry_t *entry = &curr->entries[0];
                    entry->knot_ids[0] = 0;
                    entry->idx = param.counter;

                    entry->search_type = j;

                    entry->start = -1;
                    entry->end = -1;

                    entry->start_t2 = -1;
                    entry->end_t2 = -1;

                    entry->length = -1;

                    //writes knot_ids inside entry
                    KNTID_print_knot(entry->knot_ids, IDS_MAXLEN, knot_type);
                } else {

                    param.search[j].LocFnc_ptr(
                            &closed_arc,
                            knt_rect,
                            param.search[j].st_p,
                            param.search[j].end_p,
                            param.search[j].close_subchain_ptr,
                            param.kntid_ws
                    );

                    cnode->sres[j] = report_search_results(
                            &closed_arc,
                            j,
                            param.counter,
                            &param
                    );
                }

                //printf("res report: %p\n\n", res->entries[i]);
            }
        }

        srlist_push(res, cnode);

        KNTfree_arc(&closed_arc);
        KNTfree_arc(arc_ptr);
        KNTfree_arc(knt_rect);
        qhull_terminate();
        param.counter++;
    }

    kymoknot_terminate(&param);
    return res;
}


search_retval_ll_t *KymoKnot_ring(
        search_config_t *s_config,
        search_data_t *s_data
) {
    int i;

    KNTid knot_type;  // knot identifier. See KNT_identify.h, KNT_table.h
    KNTarc *knt_rect;
    KNTarc *knt_ptr;
    search_data_entry_t *ent;

    search_retval_ll_t *res;
    res = srlist_init();

    struct param_t param;
    kymoknot_initialize_python(&param, s_config);

    for (i = 0; i < s_data->len; i++) {

        search_retval_llnode_t *  cnode = srnode_init();

        ent = s_data->entries[i];
        knt_ptr = KNTIO_mat_to_arc_ring(ent->mat, ent->len);

        if (knt_ptr == NULL) {
            failed("Cannot allocate memory for arc_ring");
        }

        set_search_brackets_ring(&param, param.counter, knt_ptr->len);
        //allocate qhull working space
        qhull_init(3 * (knt_ptr->len + MAX_CLS_POINTS));
        //close chain and rotate it
        KNTLcentre_rotate_random(knt_ptr);
        //--rectification (excluding first and last bead)
        int start_local;
        int end_local;
        //XXX this condition needs to be improved
        if (param.f_arc_start || param.f_arc_end) {
            start_local = param.arc_start;
            end_local = param.arc_end;
        } else {
            start_local = 0;
            end_local = knt_ptr->len - 1;
            param.arc_start = start_local;
            param.arc_end = end_local;
        }

        if (param.f_max_stride == FALSE) {
            param.max_stride = knt_ptr->len / 50;
        }
        knt_rect = KNTLrectify_coord_local(knt_ptr, start_local, end_local, param._min_stride, param.max_stride);
        int start = get_idx_rect_chain(knt_rect, start_local);
        int end = get_idx_rect_chain(knt_rect, end_local);
        //
        fprintf(stderr, "knt_ptr->len %d -- knt_rect->len %d\n", knt_ptr->len, knt_rect->len);
        //--compute knot type of closed portion
        knot_type = KNTID_identify_knot(knt_rect, param.kntid_ws);
        knt_ptr->knot_type = knt_rect->knot_type;
        //--bracketing on rectified chain
        //--Begin the search
        for (int j = 0; j < N_SEARCHES; j++) {

            if (param.search_type[j]) {

                if (param.f_arc_start || param.f_arc_end) {
                    param.search[j].st_p = start;
                    param.search[j].end_p = end;
                } else {
                    param.search[j].st_p = DONT_CARE;
                    param.search[j].end_p = DONT_CARE;
                }
                param.search[j].S = param.max_stride;
                param.search[j].fout = NULL;

                if (knot_type.k_id == K_Un) {

                    search_retval_entry_t *curr;

                    curr = init_search_results(1);
                    cnode->sres[j] = curr;

                    knt_entry_t *entry = &curr->entries[0];
                    entry->knot_ids[0] = 0;
                    entry->idx = param.counter;

                    entry->search_type = j;

                    entry->start = -1;
                    entry->end = -1;

                    entry->start_t2 = -1;
                    entry->end_t2 = -1;

                    entry->length = -1;

                    //writes knot_ids inside entry
                    KNTID_print_knot(entry->knot_ids, IDS_MAXLEN, knot_type);

                } else {

                    param.search[j].LocFnc_ptr(
                            knt_ptr,
                            knt_rect,
                            param.search[j].st_p,
                            param.search[j].end_p,
                            param.search[j].close_subchain_ptr,
                            param.kntid_ws
                    );

                    cnode->sres[j] = report_search_results(
                            knt_ptr,
                            j,
                            param.counter,
                            &param
                    );

                }

                //printf("res report: %p\n\n", res->entries[i]);
            }
        }

        srlist_push(res, cnode);

        KNTfree_arc(knt_ptr);
        KNTfree_arc(knt_rect);
        qhull_terminate();
        param.counter++;
    }
    kymoknot_terminate(&param);

    return res;
}


void free_search_retval(search_retval_ll_t * search_results) {

    int i;
    search_retval_llnode_t * node, * tmp;

    node = search_results->head;
    while(node != NULL) {

        for(i=0; i<N_SEARCHES; i++) {

            if (node->sres[i]) {
                free(node->sres[i]);
            }

        }

        tmp = node->next;
        free(node);
        node = tmp;
    }

    free(search_results);
}


close_retval_t *init_close_retval(size_t len) {

    close_retval_t *res;
    res = malloc(sizeof(*res));

    if (res == NULL) {
        failed("Cannot allocate memory for close retval");
    }

    res->entries = malloc(len * sizeof(*res->entries));
    res->len = len;

    if (res == NULL) {
        failed("Cannot allocate memory for search retval");
    }

    return res;
}


void free_close_retval(close_retval_t *clretval) {

    int i;

    for (i = 0; i < clretval->len; i++) {
        free(clretval->entries[i].coord);
    }
    free(clretval->entries);
    free(clretval);
}


close_retval_t *KymoKnot_close(close_data_t *c_data) {

    close_retval_t *res;
    search_data_entry_t *in;
    close_retval_entry_t *out;

    KNTarc *arc_ptr;
    KNTarc closed_arc;
    int i, j, k;
    int memsize;

    res = init_close_retval(c_data->len);

    for (k = 0; k < c_data->len; k++) {

        //printf("Closing chain %d\n", k);

        in = c_data->entries[k];
        out = &res->entries[k];

        /*read one chain at a time from input file. Main loop */
        if ((arc_ptr = KNTIO_mat_to_arc_linear(in->mat, in->len)) != NULL) {
            /*allocate qhull working space*/
            qhull_init(3 * arc_ptr->len);
            closed_arc = KNTCqhull_hybrid_close_subchain(arc_ptr, arc_ptr->start, arc_ptr->end);

            out->len = closed_arc.len + 1;

            memsize = sizeof(*out->coord) * 3 * out->len;
            out->coord = malloc(memsize);

            if (out->coord == NULL) {
                failed("Cannot allocate memory for KymoKnot_close retval");
            }

            //Copy all coordinates from KNTarc to return structure
            for (i = 0; i < closed_arc.len; i++) {
                for (j = 0; j < 3; j++) {
                    out->coord[i * 3 + j] = closed_arc.coord[i][j];
                }
            }

            //Last row which is equal to the first, closing the loop
            for (j = 0; j < 3; j++) {
                out->coord[closed_arc.len * 3 + j] = closed_arc.coord[0][j];
            }

            KNTfree_arc(&closed_arc);
            KNTfree_arc(arc_ptr);
            qhull_terminate();
        }
    }

    return res;
}



