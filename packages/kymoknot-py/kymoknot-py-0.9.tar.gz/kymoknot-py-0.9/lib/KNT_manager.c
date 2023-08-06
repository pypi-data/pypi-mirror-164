#include "KNT_manager.h"
#include "KNT_defaults.h"
#include "KNT_arc.h"
#include "KNT_lib.h"
#include "KNT_closures.h"
#include "KNT_io.h"
#include "messages.h"
#include "prng.h"
#include <libgen.h>
#include <math.h>
#include <string.h>
#include <getopt.h>
#include <time.h>
#include <ctype.h>
#include <unistd.h>

#define  _GNU_SOURCE

#include <stdio.h>
#include <stdlib.h>

#include "KymoKnot_bindings.h"


/*---DEFAULT values for the 3 type of searches implemented --*/
const searchManager_t BUsearch_DEFAULT = {
        DONT_CARE,
        DONT_CARE,
        0,
        KNTCqhull_hybrid_close_subchain,
        KNTL_BUloc_rect1,
        ARC_ID_SK,
        "BU_",
        "Bottom-up search",
        "",
        NULL};

const searchManager_t TDsearch_DEFAULT = {
        DONT_CARE,
        DONT_CARE,
        0,
        KNTCqhull_hybrid_close_subchain,
        KNTL_TDloc_rect1,
        ARC_ID_SCK,
        "TD_",
        "Top-down search",
        "",
        NULL};

const searchManager_t UNSsearch_DEFAULT = {
        DONT_CARE,
        DONT_CARE,
        0,
        KNTCqhull_hybrid_close_subchain,
        KNTL_UNSloc_rect1,
        ARC_ID_SKU,
        "UNS_",
        "Bottom-up search - no check on complementary arc",
        "",
        NULL};

const searchManager_t TNGsearch_DEFAULT = {
        DONT_CARE,
        DONT_CARE,
        0,
        KNTCqhull_hybrid_close_subchain,
        KNTL_TNGloc_rect1,
        ARC_ID_TNG,
        "TNG_",
        "Tangle search (bottom-up) - check on complementary arc of knot\n each tangle has 4 points: start_1 end_1 start_2 end2",
        "",
        NULL};

void print_help() {
    fprintf(stderr, " \n");
    fprintf(stderr, "%sKymoKnot version %s\n\nLocates the knotted portion on a chain.\n", __DATE__, _VERSION_);
    fprintf(stderr,"Use KymoKnot_linear.x for liner chains, KymoKnot_ring.x for circular ones.\n");
    fprintf(stderr,
            "The programs identify the knotted portion according to different search schemes [1].\n");
    fprintf(stderr,
            "These schemes identify different entanglement properties of a chain\n and may in general give different results.");
    fprintf(stderr, "For a detailed study, see ref [2].\n");
    fprintf(stderr,
            "The bottom-up, top-down and  'unsafe' bottom-up search schemes can be used.\n");
    fprintf(stderr, " Bottom up is enabled by default if no search scheme is specified by the user.\n");
    fprintf(stderr, "\nPlease cite:\n");
    fprintf(stderr, "Tubiana L., Polles G., Orlandini E, Micheletti C.,\n" );
    fprintf(stderr, "KymoKnot: A web server and software package to identify and locate knots in trajectories of linear or circular polymers\n");
    fprintf(stderr, "EPJE 41(6) 2018, https://link.springer.com/article/10.1140/epje/i2018-11681-0\n");
    fprintf(stderr, "\n[1] Tubiana L., Orlandini E, Micheletti C\n");
    fprintf(stderr,
            "Probing the Entanglement and Locating Knots in Ring Polymers: A Comparative Study of Different Arc Closure Schemes\n");
    fprintf(stderr,
            "Progress of Theoretical Physics supplement, 192, 192-204 (2011)\nhttp://ptp.ipap.jp/link?PTPS/191/192\n");
    fprintf(stderr, "\n[2] Tubiana L., Orlandini E, Micheletti C\n");
    fprintf(stderr, "Multiscale entanglement in ring polymers under spherical confinement\n");
    fprintf(stderr, "Phys. Rev. Lett. 107, pg 188302 (2011).\nhttp://prl.aps.org/pdf/PRL/v107/i18/e188302\n");
    fprintf(stderr, "-------------------------------------------------------\n");
    fprintf(stderr, "usage:\n");
    fprintf(stderr, "\tKymoKnot_linear.x [options] input_file   # for linear chains\n");
    fprintf(stderr, "\tKymoKnot_ring.x [options] input_file   # for circular chains\n");
    fprintf(stderr, "\ninput file must be in the format:\n\tN\n\tx y z\n\tx y z\n\t...\n");
    fprintf(stderr, "where N is the length of the coordinate sets.\n");
    fprintf(stderr, "If the input files contain coordinate of rings, the edges\n");
    fprintf(stderr, "x_0 y_0 z_0 and x_(N-1) y_(N-1) z_(N-1) must coincide.\n");
    fprintf(stderr, "Several configurations can be given one after the other in the same input file\n");
    fprintf(stderr, "\n");
    fprintf(stderr, "OUTPUT\n");
    fprintf(stderr, "BU_  [ -b option ]: shortest knotted portion. Bottom-up search\n");
    fprintf(stderr, "UNS_ [ -u option ]:  bottom-up search, without unknottedness check on complementar arc\n");
    fprintf(stderr, "TD_  [ -t option ]: shortest continuosly knotted portion. Top-down search\n");
    fprintf(stderr, "TNG_  [ -x option ]: shortest tangle. bottom-up search\n");
    fprintf(stderr, "OUTPUT FILE FORMAT:\n i Adet_1 Adet_2 K_id start end Length\n");
    fprintf(stderr, " where i is the index of the chain; Adet_1 and Adet_2 are the Alexander determinants,\n");
    fprintf(stderr, " K_id the knot id according to KNT_table.h; start, end, and length are the starting point,\n");
    fprintf(stderr, " ending point and length of the knotted portion.\n");
    fprintf(stderr, " If more portions are found they are print on the same line.\n");
    fprintf(stderr, "-------------------------------------------------------\n");
    fprintf(stderr, "OPTIONS: \n");
    fprintf(stderr, "\t-h:\t\t print this help and exit.\n");
    fprintf(stderr,
            "\t-s <max_stride>:\t maximum stride for rectification. Default is 2%% of the chain length. Negative values in input set the stride to unlimited \n");
    fprintf(stderr,
            "\t-m <mem_size>:\t USE WITH CAUTION! Set the size of memory manually. Insert the expected length of the chain after simplification. \n");
    fprintf(stderr, "\t-r <seed>:\t set the pseudo random number generator's seed. Default: use time()+getpid().\n");
    fprintf(stderr, "\t-F <start>:\t (use in conjunction with -T) set the starting point for knot localization. \n");
    fprintf(stderr, "\t-T <end>:\t (use in conjunction with -F) set the ending point for knot localization.\n");
    fprintf(stderr, "\t-b:\t Perform bottom-up search. ( DEFAULT ) \n");
    fprintf(stderr, "\t-t:\t Perform top-down search.  \n");
    fprintf(stderr, "\t-u:\t Perform bottom-up search without checking the complementar arc.\n");
    fprintf(stderr, "\t-x:\t Perform tangle search ( bottom-up). ONLY AVAILABLE ON LINEAR CHAINS. \n");
    fprintf(stderr, "\t\t Note that the tangle search first identifies a BU knot, circularizes the chain with a qhull closure\n\t\t and later look again for a BU knot which includes the closure arc. This second knot is found using\n\t\t a bridge closure");
    fprintf(stderr, " \n");
}

void set_default_behaviour(struct param_t *param) {
    param->_min_stride = 2;
    param->_simp_sweeps = 4;
    //modifiable by options
    param->arc_start = DONT_CARE;
    param->arc_end = DONT_CARE;
    param->max_stride = 0;
    param->fin_prev_search = NULL;
    param->print_conf = FALSE;
    param->memlen = MEMLEN;
    param->closure_type = CL_QHULLHYB[0];
    param->seed = time(NULL) + getpid();
    param->search_type[BU] = TRUE;
    param->search_type[TD] = FALSE;
    param->search_type[UNS] = FALSE;
    param->search_type[TNG] = FALSE;
    param->search[BU] = BUsearch_DEFAULT;
    param->search[TD] = TDsearch_DEFAULT;
    param->search[UNS] = UNSsearch_DEFAULT;
    param->search[TNG] = TNGsearch_DEFAULT;
    param->counter = 0;
    param->kntid_ws = NULL;
    param->f_arc_start = FALSE;
    param->f_arc_end = FALSE;
    param->f_prev_search = FALSE;
    param->f_max_stride = FALSE;
}

void read_command_line(struct param_t *param, int argc, char **argv) {
    int c;
    int search_type[N_SEARCHES];
    for (int i = 0; i < N_SEARCHES; i++) {
        search_type[i] = FALSE;
    }
    if (argc < 2) {
        print_help();
        exit(1);
    }

    /*--open input file --*/
    sprintf(param->filename, "%s", argv[argc - 1]);
    if ((param->fin = fopen(param->filename, "r")) == NULL) {
        printf("Could not open file %s .\n", param->filename);
        exit(1);
    }

    /*---GETOPT--------------------------------------------*/
    while ((c = getopt(argc, argv, "hbutxdc:s:m:r:F:T:P:")) != -1) {
        switch (c) {
            case 'h':
                print_help();
                break;
            case 'F':
                param->arc_start = atoi(optarg);
                param->f_arc_start = TRUE;
                break;
            case 'T':
                param->arc_end = atoi(optarg);
                param->f_arc_end = TRUE;
                break;
            case 'P':
                sprintf(param->fname_prev_search, "%s", optarg);
                param->f_prev_search = TRUE;
                if ((param->fin_prev_search = fopen(param->fname_prev_search, "r")) == NULL) {
                    failed("Can not open file passed with option -P.");
                }
                //this must become a function.
                size_t len = 2048;
                char *hdr = (char *) malloc(len);
                getline(&hdr, &len, param->fin_prev_search);
                getline(&hdr, &len, param->fin_prev_search);
                free(hdr);
                //
                break;
            case 's':
                param->max_stride = atoi(optarg);
                param->f_max_stride = TRUE;
                param->_min_stride = (int) floor(param->max_stride / pow(2, param->_simp_sweeps));
                param->_min_stride = (param->_min_stride > 3) ? param->_min_stride : 2;
                break;
            case 'b':
                search_type[BU] = TRUE;
                break;
            case 't':
                search_type[TD] = TRUE;
                break;
            case 'u':
                search_type[UNS] = TRUE;
                break;
            case 'x':
                search_type[TNG] = TRUE;
                fprintf(stderr,"Warning: Tangle search is experimental.\n");
                break;
            case 'm':
                param->memlen = atoi(optarg);
                fprintf(stderr, "Warning: Memory will be allocated to store %d beads.\n", param->memlen);
                fprintf(stderr, "Segmentation faults may result if the memory is not sufficient\n");
                break;
            case 'd':
                param->print_conf = TRUE;
                break;
            case 'c':
                param->closure_type = optarg[0];
                break;
            case 'r':
                param->seed = atoi(optarg);
                break;
            case '?':
                if (optopt == 'c')
                    fprintf(stderr,
                            "Option -%c requires an argument.\n",
                            optopt);
                else if (isprint(optopt))
                    fprintf(stderr,
                            "Unknown option `-%c'.\n",
                            optopt);
                else
                    fprintf(stderr,
                            "Unknown option character `\\x%x'.\n",
                            optopt);
                exit(1);
            default:
                abort();
        }
    }
    //Other checks.
    if (param->f_arc_start && param->arc_start < 0) {
        failed("Search starting point (-F) can not be negative.");
    } else if (param->f_arc_end && param->arc_end < 0) {
        failed("Search ending point (-T) can not be negative.");
    }
    //Set searches.
    int reset_searches = FALSE;
    for (int i = 0; i < N_SEARCHES; i++) {
        if (search_type[i] != FALSE) {
            reset_searches = TRUE;
            break;
        }
    }
    if (reset_searches) {
        for (int i = 0; i < N_SEARCHES; i++) {
            param->search_type[i] = search_type[i];
        }
    }
}

/*
void set_option_behaviour (struct param_t *param, struct options_t *options)
{
    if (options->f_arc_start )
    {
        if(options->arc_start>=0)
            param->arc_start=options->arc_start;
        else
            failed("Invalid value for polymer portion to search. Start <0!");
    }
    if (options->f_arc_end  ) param->arc_end=options->arc_end;
    if (options->f_seed         ) param->seed=options->seed;
    if (options->print_conf )   param->print_conf=TRUE;
    if (options->f_arc_start && options->f_arc_end && options->arc_end <= options->arc_start)
    {
        failed("Invalid values for polymer portion to search: end <= start!");
    }
    if (options->f_max_stride )
    {
      param->max_stride  = options->max_stride;
      param->_min_stride = (int)floor( param->max_stride/pow(2,param->_simp_sweeps));
      param->_min_stride = (param->_min_stride > 3) ? param->_min_stride : 2 ;
    }
    if (options->memlen>0)
    {
        param->memlen=options->memlen;
        fprintf(stderr,"Warning: Memory will be allocated to store %d beads.\n",param->memlen);
        fprintf(stderr,"Segmentation faults may result if the memory is not sufficient\n");
    }
    //unset default searches if any is specified
    for(int i=0;i<N_SEARCHES;i++)
    {
        if(options->search_type[i])
        {
            for(int j=0;j<N_SEARCHES;j++)
            {
                param->search_type[j]=FALSE;
            }
            break;
        }
    }
    //set specified searches
    for(int i=0;i<N_SEARCHES;i++)
    {
        if(options->search_type[i])
        {
            param->search_type[i]=TRUE;
        }
    }
    //I know this is quite ugly, but it works.
    if (options->f_prev_search)
    {
        if((param->fin_prev_search=fopen(options->fname_prev_search,"r"))==NULL)
        {
            failed ("Can not open file passed with option -P.");
        }
        int len=2048;
        char *hdr= (char *) malloc(len);
        getline(&hdr,&len,param->fin_prev_search);
        getline(&hdr,&len,param->fin_prev_search);
        char *stride;//=strstr(hdr,"stride:");
        if((stride=strtok(hdr,"s"))==NULL)
            { failed("Error while processing header. Check source code");}
        if((stride=strtok(NULL,":"))==NULL)
            { failed("Error while processing header. Check source code");}
        if((stride=strtok(NULL,":"))==NULL)
            { failed("Error while processing header. Check source code");}
        if((stride=strtok(NULL,"a"))==NULL)
            { failed("Error while processing header. Check source code");}
        param->prev_stride=atoi(stride);
        getline(&hdr,&len,param->fin_prev_search);
        //Now I have finished with the header.
        free(hdr);
        fprintf(stderr,"previous stride: %d\n",param->prev_stride);
    }
    //
    for(int i=0; i<N_SEARCHES;i++)
    {
        if(options->search_type[i]>0){param->search_type[i]=TRUE;}
    }
    // I will treat closure types later on.
    //case 'c':
    //if (strcmp(optarg,CL_QHULLHYB) == 0)
    //{
    //cls_type = 'H';
    //fprintf(stdout,"closure type: %s\n",CL_QHULLHYB);
    //}
    //else if (strcmp(optarg,QHULLCLOSURE) == 0)
    //{
    //cls_type = 'Q';
    //fprintf(stdout,"closure type: %s\n",QHULLCLOSURE);
    //}
    //else if (strcmp(optarg,BRIDGECLOSURE) == 0)
    //{
    //cls_type = 'B';
    //fprintf(stdout,"closure type: %s\n",BRIDGECLOSURE);
    //}
    //else if (strcmp(optarg,RADIALCLOSURE) == 0)
    //cls_type = 'R';
    //else if (strcmp(optarg,STCHCLOSURE) == 0)
    //{
    //cls_type = 'S';
    //flag_stch = 1;
    //fprintf(stdout,"closure type: %s\n",STCHCLOSURE);
    //}
    //else
    //failed("closure type not recognized");
    //failed("Not implemented yet..sorry\n");
    //break;
}
*/

void settings2string(char *string, struct param_t *param) {
    time_t t = time(NULL);
    struct tm tm = *localtime(&t);
    sprintf(string, "#%d-%d-%d %d:%d:%d -- ", tm.tm_year + 1900, tm.tm_mon + 1, tm.tm_mday, tm.tm_hour, tm.tm_min,
            tm.tm_sec);
    if (param->f_max_stride == FALSE) {
        sprintf(string, "%s seed: %d \tmax_stride: auto (2%%) \tarc_start: %d \tarc_end: %d \tclosure: %c\n", string,
                param->seed, param->arc_start, param->arc_end, param->closure_type);
    } else if (param->max_stride >= 0) {
        sprintf(string, "%s seed: %d \tmax_stride: %d \tarc_start: %d \tarc_end: %d \tclosure: %c\n", string,
                param->seed, param->max_stride, param->arc_start, param->arc_end, param->closure_type);
    } else {
        sprintf(string, "%s seed: %d \t max_stride: unlimited: \t arc_start: %d \t arc_end: %d \tclosure: %c\n", string,
                param->seed, param->arc_start, param->arc_end, param->closure_type);
    }
}

void settings2stderr(char *string, struct param_t *param) {
    fprintf(stderr, "%s", string);
    fprintf(stderr, "Performing the following knot_searches:\n");
    for (int i = 0; i < N_SEARCHES; i++) {
        if (param->search_type[i]) {
            fprintf(stderr, "%s\n", param->search[i].fout_expl);
            fprintf(stderr, "file prefix: %s_ \n\n", param->search[i].fout_prefix);
        }
    }
}

/*
void locknot_global_init (char *settingsString)
{
  if ((param._fin=fopen(param.filename,"r"))==NULL)
  {
    printf("Could not open file %s .\n",param.filename);
    exit(1);
  }
  initialize_prng ( param.seed );
    KNTID_ws_var knt_id_ws_param={2*param.memlen,1100};
    KNTID_wspace    *kntid_ws=KNTID_wspace_init(&knt_id_ws_param);
}
*/

void searchManagers_init(struct param_t *param, char *settingsString) {
    char *bname;
    char *dname;
    char outname[1024];
    FILE *fout;

    bname = basename(param->filename);
    dname = dirname(param->filename);
    for (int i = 0; i < N_SEARCHES; i++) {
        if (param->search_type[i] > 0) {
            outname[0] = '\0';
            param->search[i].st_p = param->arc_start;
            param->search[i].end_p = param->arc_end;
            param->search[i].S = param->max_stride;
            sprintf(outname, "%s/%s_%s", dname, param->search[i].fout_prefix, bname);
            if ((fout = fopen(outname, "w")) == NULL) {
                printf("Could not open file %s .\n", outname);
                exit(1);
            }
            fprintf(fout, "#%s\n", param->search[i].fout_expl);
            fprintf(fout, "%s", settingsString);
            fprintf(fout, "# index Adet_1 Adet_2 Knot_id\t start end length\n");
            fflush(fout);
            param->search[i].fout = fout;
        }
    }
}

void kymoknot_initialize_cli(struct param_t *param, int argc, char **argv) {
    char setting_string[512];
    set_default_behaviour(param);
    read_command_line(param, argc, argv);
    settings2string(setting_string, param);
    settings2stderr(setting_string, param);
    searchManagers_init(param, setting_string);
    initran_(&param->seed);
    KNTID_ws_var knt_id_ws_param = {2 * param->memlen, 1000};
    param->kntid_ws = KNTID_wspace_init(&knt_id_ws_param);
}


void set_search_params(struct param_t *param, search_config_t *cl_params) {

    if (cl_params->chain_file_path) {

        strncpy(param->filename, cl_params->chain_file_path, 1024);
        if ((param->fin = fopen(param->filename, "r")) == NULL) {
            printf("Could not open file %s .\n", param->filename);
            exit(1);
        }
    }
    else {
        param->filename[0] = 0;
        param->fin = NULL;
    }

    param->f_arc_start = cl_params->f_arc_start;
    param->arc_start = cl_params->arc_start;

    param->f_arc_end = cl_params->f_arc_end;
    param->arc_end = cl_params->arc_end;

    //param->f_prev_search = cl_params->f_prev_search;
    //param->fname_prev_search[0] = 0;
    //param->fin_prev_search = NULL;

    param->max_stride = cl_params->max_stride;
    param->f_max_stride = cl_params->f_max_stride;
    param->_min_stride = cl_params->_min_stride;
    param->_simp_sweeps = cl_params->_simp_sweeps;

    for (int i = 0; i < N_SEARCHES; i++) {
        param->search_type[i] = cl_params->search_type[i];
        param->search[i].close_subchain_ptr = str_to_closure_func(
                cl_params->close_subchain,
                CL_STR_MAXLEN
                );

        //performed again in KymoKnot_linear
        //
        //param->search[i].st_p = param->arc_start;
        //param->search[i].end_p = param->arc_end;
        //param->search[i].S = param->max_stride;
        //param->search[i].fout = NULL;
    }

    param->memlen = cl_params->memlen;

    param->print_conf = cl_params->print_conf;

    param->closure_type = cl_params->closure_type[0];

    param->seed = cl_params->seed;

    //Other checks.
    if (param->f_arc_start && param->arc_start < 0) {
        failed("Search starting point (-F) can not be negative.");
    } else if (param->f_arc_end && param->arc_end < 0) {
        failed("Search ending point (-T) can not be negative.");
    }

}


void kymoknot_initialize_python(struct param_t *param, search_config_t *cl_params) {
    char setting_string[512];

    //Load the defaults in params
    set_default_behaviour(param);

    //set cmdlines arguments in params
    set_search_params(param, cl_params);

    settings2string(setting_string, param);
    settings2stderr(setting_string, param);
    //searchManagers_init         (param, setting_string);
    initran_(&param->seed);
    KNTID_ws_var knt_id_ws_param = {2 * param->memlen, 1000};
    param->kntid_ws = KNTID_wspace_init(&knt_id_ws_param);
}


void kymoknot_terminate(struct param_t *param) {
    // free memory
    KNTID_free_wspace(param->kntid_ws);
    // close files
    if (param->fin) {
        fclose(param->fin);
    }

    if (param->f_prev_search) {
        fclose(param->fin_prev_search);
    }

    for (int i = 0; i < N_SEARCHES; i++) {
        if (param->search_type[i]) {
            if (param->search[i].fout) {
                fclose(param->search[i].fout);
            }
        }
    }
}

void set_search_brackets_linear(struct param_t *param, int cnt, int arc_len) {
    if (param->f_prev_search) {
        size_t len = 1024;
        char *prev_line = (char *) malloc(len);
        getline(&prev_line, &len, param->fin_prev_search);
        char *tok;
        if ((tok = strtok(prev_line, " \t")) == NULL) {
            failed("Error reading knot position input file");
        }
        for (int i = 0; i < 3; i++) {
            if ((tok = strtok(NULL, " \t")) == NULL) {
                failed("Error reading knot position input file");
            }
        }
        if ((tok = strtok(NULL, " \t")) == NULL) {
            failed("Error reading knot position input file");
        }
        param->arc_start = atoi(tok);
        if ((tok = strtok(NULL, " \t")) == NULL) {
            failed("Error reading knot position input file");
        }
        param->arc_end = atoi(tok);
        if ((tok = strtok(NULL, " \t")) == NULL) {
            failed("Error reading knot position input file");
        }
        int kl = atoi(tok);
        param->arc_start -= arc_len / 20;
        param->arc_end += arc_len / 20;
        if (param->arc_start < 0) { param->arc_start = 0; }
        free(prev_line);
        fprintf(stderr, "CONF %d. search brackets: %d %d\n", cnt, param->arc_start, param->arc_end);
    }
    //check on bracketing
    if (param->f_arc_start == FALSE) {
        param->arc_start = 0;
    }
    if (param->f_arc_end == FALSE) {
        param->arc_end = arc_len - 1;
    }
    if (param->arc_end >= arc_len) {
        failed("End of specified search region out of boundaries.");
        param->arc_end = arc_len - 1;
    } else if (param->arc_start < 0) {
        failed("start of specified search region out of boundaries.");
    } else if (param->arc_end <= param->arc_start) {
        failed("Invalid values for polymer portion to search: end <= start!");
    }
}

void set_search_brackets_ring(struct param_t *param, int cnt, int arc_len) {
    if (param->f_arc_start) {
        if (param->arc_start >= arc_len || param->arc_start < 0) {
            failed("Out of boundaries search starting point.\n");
        } else if (!param->f_arc_end) {
            param->arc_end = param->arc_start - 1 > 0 ? param->arc_start : 0;
        }
    }
    if (param->f_arc_end) {
        if (param->arc_end >= arc_len || param->arc_end < 0) {
            failed("Out of boundaries search ending point.\n");
        } else if (!param->f_arc_start) {
            param->arc_start = param->arc_end + 1 < arc_len ? param->arc_end + 1 : 0;
        }
    }
    if (param->f_prev_search) {
        size_t len = 1024;
        char *prev_line = (char *) malloc(len);
        getline(&prev_line, &len, param->fin_prev_search);
        char *tok;
        if ((tok = strtok(prev_line, " \t")) == NULL) {
            failed("Error reading knot position input file");
        }
        for (int i = 0; i < 3; i++) {
            if ((tok = strtok(NULL, " \t")) == NULL) {
                failed("Error reading knot position input file");
            }
        }
        if ((tok = strtok(NULL, " \t")) == NULL) {
            failed("Error reading knot position input file");
        }
        param->arc_start = atoi(tok);
        if ((tok = strtok(NULL, " \t")) == NULL) {
            failed("Error reading knot position input file");
        }
        param->arc_end = atoi(tok);
        if ((tok = strtok(NULL, " \t")) == NULL) {
            failed("Error reading knot position input file");
        }
        int kl = atoi(tok);
        param->arc_start -= arc_len / 20;
        param->arc_end += arc_len / 20;
        if (param->arc_start < 0) { param->arc_start = 0; }
        free(prev_line);
        fprintf(stderr, "CONF %d. search brackets: %d %d\n", cnt, param->arc_start, param->arc_end);
    }
    //check on bracketing
    if (param->arc_end > arc_len) {
        failed("End of specified search region out of boundaries.");
    }
}

int get_idx_rect_chain(KNTarc *knt_rect, int idx_orig) {
    for (int i = 0; i < knt_rect->len; i++) {
        if (idx_orig == knt_rect->index[i]) {
            return i;
        }
    }
    return -1;
}

void print_search_results_linear(KNTarc *knt_ptr, searchManager_t *sM, int cnt, struct param_t *param) {
    KNTarc *knt_here = knt_ptr;
    int start, end;
    char line[1024];
    int bfs = 128;
    char knot_ids[bfs];
    //2CHECK This need to be improved with a double check on the knot type.
    sprintf(line, "%d ", cnt);
    do {
        if (knt_here->arc_type == sM->arc_id) //identified by search type arc_id
        {
            start = knt_here->start + param->arc_start;
            end = knt_here->end + param->arc_start;
            KNTid K = knt_here->knot_type;
            //K=KNTID_get_knot_from_id(K.k_id);
            KNTID_print_knot(knot_ids, bfs, K);
            if(sM->arc_id == ARC_ID_TNG) {
                int start_t2 = knt_here->start_t2 + param->arc_start;
                int end_t2 = knt_here->end_t2 + param->arc_start;
                int len1 = (start_t2 > start) ? start_t2 - start : start - start_t2 + knt_ptr->len;
                int len2 = (end > end_t2) ? end - end_t2 : end_t2 - end + knt_ptr->len;
                sprintf(line, "%s\t%s %d %d %d %d %d \t", line,
                        knot_ids,
                        start,
                        start_t2,
                        end_t2,
                        end,
                        len1+len2);
            }
            else {
                sprintf(line, "%s\t%s %d %d %d \t",
                        line,
                        knot_ids,
                        start,
                        end,
                        (end > start) ? end - start : end - start + knt_ptr->len);
            }
            if (param->print_conf) {
                fprintf(stderr, "--------------\n");
                KNTIOprint_arc(stderr, knt_ptr, start, end);
                fprintf(stderr, "--------------\n");
            }
        }
        knt_here = knt_here->next;
    } while (knt_here != NULL);
    fprintf(sM->fout, "%s\n", line);
    fflush(sM->fout);
}


search_retval_entry_t *init_search_results(int res_nr) {

    search_retval_entry_t *res;
    res = malloc(sizeof(search_retval_entry_t));

    if (res == NULL) {
        failed("Cannot allocate memory for search_retval_entry_t");
    }

    res->len = res_nr;
    res->entries = malloc(res->len * sizeof(knt_entry_t));

    if (res->entries == NULL) {
        failed("Cannot allocate memory for search_retval_entry_t->entires");
    }

    return res;
}


void free_retval_entry(search_retval_entry_t *report) {
    free(report->entries);
    free(report);
}


search_retval_entry_t *report_search_results(
        KNTarc *knt_ptr,
        int search_type,
        int cnt,
        struct param_t *param
) {

    char arc_id;
    int entries_nr, i;
    int start, end;
    KNTarc *knt_here;

    search_retval_entry_t *res;

    arc_id = param->search[search_type].arc_id;

    knt_here = knt_ptr;
    entries_nr = 0;
    while (knt_here != NULL) {

        if (knt_here->arc_type == arc_id) {
            entries_nr++;
        }
        knt_here = knt_here->next;
    }

    res = init_search_results(entries_nr);

    if (entries_nr > 0) {

        knt_here = knt_ptr;
        i = 0;

        while (knt_here != NULL) {
            if (knt_here->arc_type == arc_id) {

                knt_entry_t *entry = &res->entries[i];
                entry->knot_ids[0] = 0;
                entry->search_type = search_type;

                start = knt_here->start + param->arc_start;
                end = knt_here->end + param->arc_start;

                KNTid K = knt_here->knot_type;

                KNTID_print_knot(entry->knot_ids, IDS_MAXLEN, K);

                entry->idx = cnt;
                entry->start = start;
                entry->end = end;
                entry->length = (end > start) ? end - start : end - start + knt_ptr->len;
                i++;
            }

            knt_here = knt_here->next;

        }
    }

    return res;
}


void print_search_results_ring(KNTarc *knt_ptr, searchManager_t *sM, int cnt, struct param_t *param) {
    KNTarc *knt_here = knt_ptr;;
    int start, end;
    char line[1024];
    int bfs = 128;
    char knot_ids[bfs];
    //2CHECK This need to be improved with a double check on the knot type.
    sprintf(line, "%d ", cnt);
    do {
        if (knt_here->arc_type == sM->arc_id) //identified by search type arc_id
        {
            start = knt_here->start;
            end = knt_here->end;
            KNTid K = knt_here->knot_type;
            //K=KNTID_get_knot_from_id(K.k_id);
            KNTID_print_knot(knot_ids, bfs, K);
            sprintf(line, "%s\t%s %d %d %d \t", line,
                    knot_ids, start, end, (end > start) ? end - start : end - start + knt_ptr->len);
            if (param->print_conf) {
                fprintf(stderr, "--------------\n");
                KNTIOprint_arc(stderr, knt_ptr, start, end);
                fprintf(stderr, "--------------\n");
            }
        }
        knt_here = knt_here->next;
    } while (knt_here != NULL);
    fprintf(sM->fout, "%s\n", line);
    fflush(sM->fout);
}

close_subchain str_to_closure_func(char *str, size_t maxlen) {

    close_subchain res;

    if (strncmp(str, CL_NONE, maxlen) == 0) {
        res = NULL;
    } else if (strncmp(str, CL_RING, maxlen) == 0) {
        res = NULL;
    } else if (strncmp(str, CL_BRIDGE, maxlen) == 0) {
        res = KNTCbridge_close_subchain;
    } else if (strncmp(str, CL_QHULL, maxlen) == 0) {
        res = KNTCqhull_close_subchain;
    } else if (strncmp(str, CL_QHULLHYB, maxlen) == 0) {
        res = KNTCqhull_hybrid_close_subchain;
    }

        //else if (strncmp(str, CL_RADIAL, maxlen) == 0) {
        //    res = KNTCradial_close_subchain;
        //}

    else if (strncmp(str, CL_STOCHASTIC, maxlen) == 0) {
        res = KNTCrandom_close_subchain;
    } else {
        res = NULL;
    }

    return res;
}
