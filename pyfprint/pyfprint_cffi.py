from cffi import FFI
ffi = FFI()

ffi.cdef("""
struct fp_dscv_dev;

struct fp_minutia {
	int x;
	int y;
	int ex;
	int ey;
	int direction;
	double reliability;
	int type;
	int appearing;
	int feature_id;
	int *nbrs;
	int *ridge_counts;
	int num_nbrs;
};

enum fp_enroll_result {
	FP_ENROLL_COMPLETE = 1,
	FP_ENROLL_FAIL,
	FP_ENROLL_PASS,
	FP_ENROLL_RETRY = 100,
	FP_ENROLL_RETRY_TOO_SHORT,
	FP_ENROLL_RETRY_CENTER_FINGER,
	FP_ENROLL_RETRY_REMOVE_FINGER,
};

enum fp_verify_result {
	FP_VERIFY_NO_MATCH = 0,
	FP_VERIFY_MATCH = 1,
	FP_VERIFY_RETRY = FP_ENROLL_RETRY,
	FP_VERIFY_RETRY_TOO_SHORT = FP_ENROLL_RETRY_TOO_SHORT,
	FP_VERIFY_RETRY_CENTER_FINGER = FP_ENROLL_RETRY_CENTER_FINGER,
	FP_VERIFY_RETRY_REMOVE_FINGER = FP_ENROLL_RETRY_REMOVE_FINGER,
};

int fp_init(void);
struct fp_dscv_dev **fp_discover_devs(void);
void fp_dscv_devs_free(struct fp_dscv_dev **devs);
struct fp_dev *fp_dev_open(struct fp_dscv_dev *ddev);
int fp_enroll_finger_img(struct fp_dev *dev, struct fp_print_data **print_data, struct fp_img **img);
void fp_img_free(struct fp_img *img);
void fp_print_data_free(struct fp_print_data *data);
int fp_verify_finger_img(struct fp_dev *dev, struct fp_print_data *enrolled_print, struct fp_img **img);
size_t fp_print_data_get_data(struct fp_print_data *data, unsigned char **ret);
struct fp_print_data *fp_print_data_from_data(unsigned char *buf, size_t buflen);
void fp_dev_close(struct fp_dev *dev);
void fp_exit(void);
int fp_dev_supports_print_data(struct fp_dev *dev, struct fp_print_data *data);
int fp_identify_finger_img(struct fp_dev *dev, struct fp_print_data **print_gallery, size_t *match_offset, struct fp_img **img);
void fp_img_standardize(struct fp_img *img);
struct fp_minutia **fp_img_get_minutiae(struct fp_img *img, int *nr_minutiae);
int fp_img_save_to_file(struct fp_img *img, char *path);

""")

C = ffi.dlopen('fprint')
