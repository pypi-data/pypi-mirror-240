#ifndef	tajk_data_h
#define tajk_data_h

#ifdef __cplusplus
extern "C"  {
#endif

struct stru_tajk_datafile_field2	{//新版本的接口文件字段列表,不再使用数据字典表，直接使用字段列表，把字段名等内容也放在这里，去掉没使用的描述字段
    int ver;    //版本，目前支持2.0(仅部分文件：43、44（电子合同）)、2.1和2.2，对应取值为20、21和22
    char filemode[3];//文件类型,如01,02这样
    char name[50],type;     //字段名，类型（C、A、N）
    int size,decpos;        //大小，小数位置
};

extern struct stru_tajk_datafile_field2 tajk_datafile_field2[];//数据文件和字段对应关系版本2

#ifdef __cplusplus
}
#endif

#endif
