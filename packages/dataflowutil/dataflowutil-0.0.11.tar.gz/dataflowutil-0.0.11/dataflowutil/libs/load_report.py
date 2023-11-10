import pandas as pd
from dash import Dash, html, Input, Output, ctx, callback, dcc, State, dependencies, dash_table
import dash_bootstrap_components as dbc
import os
import yaml

CHECK_ALERT_S = "S"
CHECK_ALERT_N = "N"
CHECK_ALERT_G = "G"

assets_path = os.getcwd() +'/assets'

class LoadReport():
    def __init__(self,ld):

        self.app = Dash(__name__,external_stylesheets=[dbc.themes.COSMO],suppress_callback_exceptions=True,assets_folder=assets_path)

        self.list_tags = []
        self.load_tags(ld)

        self.data = None
        
        self.icon_theme = None
        self.color_theme = None
        self.title_general = None
        self.color_df_header = None

        self.data_bucket = None
        self.data_local = None
        self.data_local_historic = None
        self.data_local_new = None


        self.df_export = None

        self.title_tab ={
            "tab-1": "1.Check Historical Data",
            "tab-2": "2.Check New Data",
        }

        self.app.callback(dependencies.Output('download_df', 'data'),
              dependencies.Input('export_df', 'n_clicks'))(self.func_download_df)
        

        self.app.callback([dependencies.Output('select_columns_historic', 'options'),dependencies.Output('select_columns_historic', 'value'),dependencies.Output("p_lengh_analysis","children"),
                           dependencies.Output('df_historic_corr', 'data'),dependencies.Output('df_historic_corr', 'columns'),dependencies.Output("count_columns_analysis","children")],
            dependencies.Input('select_db', 'value'),dependencies.State('tabs-inline', 'value'))(self.select_dataset_historic)

        self.app.callback([dependencies.Output('error_exist_columns', 'children'),
                           dependencies.Output('df_columns_check', 'data'),dependencies.Output('df_columns_check', 'columns')],
            dependencies.Input('select_columns_historic', 'value'),dependencies.State('tabs-inline', 'value'))(self.select_columns_historic)

        self.app.callback(dependencies.Output('tabs-example-content-1', 'children'),
              dependencies.Input('tabs-inline', 'value'))(self.render_content)
        
    def clear(self):
        self.data_bucket = None
        self.data_local = None
        self.data_local_historic = None
        self.data_local_new = None
        self.df_export = None

    def load_tags(self,ld):
        get_tags = ld.get_data_compare()
        self.list_tags = []
        for key,value in get_tags.items():
            if not value["update"]:
                self.list_tags.append(key)
            
    def load_interface(self,yaml_archive,data):
        with open(yaml_archive, 'r') as file:
            load_yml = yaml.safe_load(file)
        
        self.icon_theme = None
        self.color_theme = None
        self.title_general = None
        self.color_df_header = None
        self.data = data

        for key,value in load_yml.items():
            if "config_general" in  key:
                self.title_general = value["title_general"]
                self.icon_theme = value["icon"]
                self.color_theme = value["color"]
                self.color_df_header = value["color_header_df"]

        self.load_data()
        self.load_process()

    def check_columns_all_df(self,column_check):
        if column_check not in self.data_bucket.columns:
            return False
        
        if column_check not in self.data_local_historic.columns:
            return False
        
        return True

    def get_df_na_rows(self,column_check,dropna_check = False):
        merged_df = pd.merge(self.data_local_historic[f"{column_check}"], self.data_bucket[f"{column_check}"], left_index=True, right_index=True, suffixes=('_local', '_bucket'))
        different_rows = merged_df[merged_df[f'{column_check}_local'] != merged_df[f'{column_check}_bucket']]
        if dropna_check:
            different_rows = different_rows.dropna(how="all",subset=[f'{column_check}_local',f'{column_check}_bucket'])

        if different_rows[f"{column_check}_local"].shape[0] <= 0 and different_rows[f"{column_check}_bucket"].shape[0] <= 0:
            return True
        
        return False

    def get_df_negative(self,column_check,dropna_check = False):
        merged_df = pd.merge(self.data_local_historic[f"{column_check}"], self.data_bucket[f"{column_check}"], left_index=True, right_index=True, suffixes=('_local', '_bucket'))
        different_rows =  merged_df
        if dropna_check:
            different_rows = different_rows.dropna(how="all",subset=[f'{column_check}_local',f'{column_check}_bucket'])

        if different_rows[f"{column_check}_local"].shape[0] > 0 and different_rows[f"{column_check}_bucket"].shape[0] > 0:

            if different_rows[f"{column_check}_local"].dtype in ['int64', 'float64','int32', 'float32'] and different_rows[f"{column_check}_bucket"].dtype in ['int64', 'float64','int32', 'float32']:
                if (different_rows[f"{column_check}_local"] <= 0).any() or (different_rows[f"{column_check}_bucket"] <= 0).any():
                    return False

        return True
    

    def select_columns_historic(self,columns_select,tab_select):

        self.df_export = None

        if columns_select is not None:
            if len(columns_select) > 0:
                data_local = self.data_local_historic

                list_columns_bucket = self.data_bucket.columns
                list_columns_local  = self.data_local_historic.columns

                text_column = ""
                check_compare_columns = True
                if columns_select not in list_columns_bucket:
                    check_compare_columns = False
                    text_column = f"Column ( {columns_select} ) Not exist in Bucket Data"
                elif columns_select not in list_columns_local:
                    check_compare_columns = False
                    text_column =  f"Column ( {columns_select} ) Not exist in Local Data"
                else:
                    text_column = f"Column ( {columns_select} ) exist in Local and Bucket Data"
                    
                dropna = False
                if tab_select in list(self.title_tab.keys())[0]:
                    if check_compare_columns:
                        column_check = columns_select
                        merged_df = pd.merge(data_local[f"{column_check}"], self.data_bucket[f"{column_check}"], left_index=True, right_index=True, suffixes=('_local', '_bucket'))
                        different_rows = merged_df[merged_df[f'{column_check}_local'] != merged_df[f'{column_check}_bucket']]
                        if dropna:
                            different_rows = different_rows.dropna(how="all",subset=[f'{column_check}_local',f'{column_check}_bucket'])

                        get_df_negative = self.get_df_negative(column_check,dropna_check=dropna)

                        different_rows_new = different_rows.reset_index()

                        if get_df_negative:
                            self.df_export = different_rows_new
                            return "",different_rows_new.to_dict("records"),[{"name": i, "id": i,"presentation":"markdown", "type": "text"} for i in different_rows_new.columns]
                        else:
                            different_rows = merged_df
                            if different_rows[f"{column_check}_local"].shape[0] > 0 and different_rows[f"{column_check}_bucket"].shape[0] > 0:
                                if different_rows[f"{column_check}_local"].dtype in ['int64', 'float64','int32', 'float32'] and different_rows[f"{column_check}_bucket"].dtype in ['int64', 'float64','int32', 'float32']:
                                    if (different_rows[f"{column_check}_local"] <= 0).any():

                                        df_select = different_rows[different_rows[f"{column_check}_local"] <= 0]
                                        df_select = df_select.reset_index()
                                        df_end = pd.concat([different_rows_new,df_select])
                                        self.df_export = df_end
                                        return "",df_end.to_dict("records"),[{"name": i, "id": i,"presentation":"markdown", "type": "text"} for i in df_end.columns]
                                    else:
                                        if(different_rows[f"{column_check}_bucket"] <= 0).any():
                                            df_select = different_rows[different_rows[f"{column_check}_bucket"] <= 0]
                                            df_select = df_select.reset_index()
                                            df_end = pd.concat([different_rows_new,df_select])
                                            self.df_export = df_end
                                            return "",df_end.to_dict("records"),[{"name": i, "id": i,"presentation":"markdown", "type": "text"} for i in df_end.columns]
                    else:
                        return text_column,[],[]
                else:
                    data_local = self.data_local_new

                    list_columns_bucket = self.data_bucket.columns
                    list_columns_local  = data_local.columns
                    
                    
                    if columns_select in list_columns_local:
                        if data_local[columns_select].shape[0] > 0:
                            column_check = columns_select

                            data_values_unique = data_local[column_check].unique().copy()
                            df_end = pd.DataFrame(data_values_unique, columns=["Values_Uniques"])
                            df_end["Unique"] = "❌"

                            for unique_v in df_end["Values_Uniques"].unique():
                                if unique_v is not None:
                                    if column_check in list_columns_bucket:
                                        if data_local[column_check].dtype not in ['int64','float64','int32','float32']:
                                            if unique_v in self.data_bucket[column_check].unique():
                                                df_end.loc[df_end["Values_Uniques"] == unique_v, "Unique"] = "✅"
                                        
                                        if data_local[column_check].dtype in ['int64','float64','int32','float32']:
                                            if unique_v > 0:
                                                df_end.loc[df_end["Values_Uniques"] == unique_v, "Unique"] = "✅"
                            
                            self.df_export = df_end

                            return "",df_end.to_dict("records"),[{"name": i, "id": i,"presentation":"markdown", "type": "text"} for i in df_end.columns]
                    else:
                        return text_column,[],[]


        return "",[],[]


    def select_dataset_historic(self,db_name_select,tab_select):
        if db_name_select is not None:
            self.load_data(db_name_select)

            columns_bucket = set(self.data_bucket.columns)
            columns_local_historic = set(self.data_local_historic.columns)

            if tab_select in list(self.title_tab.keys())[0]:
                lengh_analysis = f"[The analysis process has begun] length analysis: {self.data_local_historic.shape[0]}"
            else:
                lengh_analysis = f"[The analysis process has begun] length analysis: {self.data_local_new.shape[0]}"

            error = 1 - abs(len(self.data_bucket.columns) - len(self.data_local.columns)) / max(len(self.data_bucket.columns) , len(self.data_local.columns))
            
            check_error = "❌" if error != 1.0 else "✅"

            check_columns = f"Columns Count: Bucket:{len(self.data_bucket.columns)} | Local:{len(self.data_local.columns)} | Status: {check_error}"
            
            dropna_check = False

            self.df_export = None

            if tab_select in list(self.title_tab.keys())[0]:
                data_local = self.data_local_historic

                list_columns_bucket = self.data_bucket.columns
                list_columns_local  = data_local.columns
                
                data_check_test = pd.DataFrame([list_columns_bucket,list_columns_local]).T
                data_check_test.rename(columns = {0:"corr_columns_data_bucket",1:"corr_columns_data_local"}, inplace = True)
                data_check_test["Checks"] = "❌"

                for key,value in dict(self.data_bucket.eq(data_local).all()).items():
                    if value:
                        data_check_test.loc[(data_check_test["corr_columns_data_bucket"] == key),"Checks"] = "✅"
                    else:
                        if self.check_columns_all_df(key):

                            get_df_check = self.get_df_na_rows(key,dropna_check=dropna_check)
                            get_df_negative = self.get_df_negative(key,dropna_check=dropna_check)

                            if get_df_check and get_df_negative:
                                data_check_test.loc[(data_check_test["corr_columns_data_bucket"] == key),"Checks"] = "✅"
            else:
                data_local = self.data_local_new

                list_columns_bucket = self.data_bucket.columns
                list_columns_local  = data_local.columns

                check_new_columns = []
                check_types = []
                check_nan = []
                check_negative = []
                check_unique = []

                if data_local.shape[0] > 0:
                    list_columns = list(list_columns_bucket.union(list_columns_local))
            
                    for i in list_columns:
                        if i in list_columns_bucket and i in list_columns_local:
                            check_new_columns.append("✅")

                            check_t = "✅" if self.data_bucket[i].dtypes == data_local[i].dtypes else "❌"
                            check_types.append(check_t)


                            check_unique_c = True
                            for unique_v in data_local[i].unique():
                                if unique_v is not None:
                                    if unique_v not in self.data_bucket[i].unique():
                                        check_unique_c = False

                            if data_local[i].dtype in ['int64','float64','int32','float32']:
                                check_unique.append("✅")
                            else:
                                if check_unique_c:
                                    check_unique.append("✅")
                                else:
                                    check_unique.append("❌")
                            
                        else:
                            check_new_columns.append("❌")
                            check_types.append("❌")
                            check_unique.append("❌")

                        if i in list_columns_local:
                            check_nan.append(data_local[i].isna().sum())

                            if data_local[i].dtype in ['int64','float64','int32','float32']:
                                check_n = "❌" if (data_local[i] <= 0).any() else "✅"
                                check_negative.append(check_n)
                            else:
                                check_negative.append("✅")
                        else:
                            check_nan.append(0)
                            check_negative.append("❌")
                    
                    data_check_test = pd.DataFrame([list_columns,check_new_columns,check_types,check_nan,check_negative,check_unique]).T
                    data_check_test.rename(columns={0:"Columns",1:"Name_Equals",2:"Types",3:"NaN",4:"Negatives",5:"Unique"},inplace=True)
                    data_check_test["NaN"] = data_check_test["NaN"].astype(int)
                else:
                    return list(columns_bucket.union(columns_local_historic)),"",lengh_analysis,[],[],check_columns

            return list(columns_bucket.union(columns_local_historic)),"",lengh_analysis,data_check_test.to_dict("records"),[{"name": i, "id": i} for i in data_check_test.columns],check_columns
        
        return [],"","",[],[],""
    
    def load_data(self,db_name_select=""):
        if len(self.list_tags) > 0:
            if len(db_name_select) <= 0:
                (data_bucket,data_local) = self.data.get_data_compare(self.list_tags[0])
            else:
                (data_bucket,data_local) = self.data.get_data_compare(db_name_select)
            self.data_bucket = data_bucket
            self.data_local = data_local
            data_bucket_shape = data_bucket.shape[0]
            self.data_local_historic = self.data_local.iloc[:data_bucket_shape]
            self.data_local_new = data_local.iloc[data_bucket_shape:]

    def func_download_df(self,n_clicks):
        if n_clicks:
            if self.df_export is not None:
                return dcc.send_data_frame(self.df_export.to_excel, "dataflowutil_report_records.xlsx", sheet_name="DataFlow Records")

    def render_content(self,tab):
        get_title = self.title_tab[tab]

        select_tag = self.list_tags[0] if len(self.list_tags) > 0 else ""

        design_historic_corr = dbc.Col(
                dbc.Row([
                    dcc.Dropdown(self.list_tags, select_tag, id='select_db',style={"margin-bottom":"5px"}),
                
                    dash_table.DataTable(
                        id='df_historic_corr',
                        editable=False,
                        page_current= 0,
                        style_table={'width': '100%', 'overflowX': 'auto',"padding-top": "17px"},
                        style_cell={'height': 'auto', 'font_family': 'Georgia','whiteSpace': 'normal','border': '1px solid grey',"color":"#232323",'textAlign': 'center'},
                        style_header={'height': 'auto','fontWeight': 'bold','border': '1px solid grey','textAlign': 'center'},
                        style_data={'height': 'auto','whiteSpace': 'normal','lineHeight': '15px'},

                        page_size= 6),
                ])
        ,width=7,style={"padding": "17px", "display":"block"})
        
        design_historic_columns = dbc.Col(
                dbc.Row([

                    dbc.Col(
                    dcc.Dropdown(id='select_columns_historic',style={"margin-bottom":"5px"}),
                    width=6),

                    dbc.Col(
                    dbc.Button("Export Result", id="export_df",color="success", className="me-1 w-100")   
                    ,width=6),

                    html.P(id="error_exist_columns", style={'textAlign': 'center'}),

                    dbc.Col(
                    dash_table.DataTable(
                        id='df_columns_check',
                        editable=False,
                        page_current= 0,
                        sort_action="native",
                        sort_mode='single',
                        #fill_width=False,
                        css=[dict(selector= "p", rule= "text-align: center; margin-bottom : 1px;")],
                        style_table={'width': '100%', 'overflowX': 'auto'},
                        style_cell={'height': 'auto', 'font_family': 'Georgia','whiteSpace': 'normal','border': '1px solid grey',"color":"#232323",'textAlign': 'center'},
                        style_header={'height': 'auto','fontWeight': 'bold','border': '1px solid grey','textAlign': 'center'},
                        style_data={'height': 'auto','whiteSpace': 'normal','lineHeight': '15px'},

                        page_size= 5),
                    width=12,style={"margin-top":"6px"})
                ])
        ,width=5,style={"padding": "17px", "display":"block"})
        

        get_render =  html.Div([

            dbc.Row(
            [
                html.H2(get_title, style={'textAlign': 'center'}),
                html.Div(style={'margin': '7px'}),

                html.P(id="p_lengh_analysis", style={'textAlign': 'center'}),
                html.P(id="count_columns_analysis", style={'textAlign': 'center'}),

                design_historic_corr,
                design_historic_columns,

            ]),
            
        ],className="d-grid gap-3 col-11 mx-auto")


        return get_render
    
    def load_process(self):
        tabs_styles = {
            'height': '44px'
        }

        tab_style = {
            'padding': '10px',
            'fontWeight': 'bold',
            "color":"#9E9E9E",
        }

        tab_selected_style = {
            'borderBottom': f'3px solid {self.color_theme}',
            'padding': '10px',
            'fontWeight': 'bold',
            "background": "white",
            "color": f"{self.color_theme}",
        }

        tabs_elements = [
            dcc.Tab(label=f'{value}', value=f'{key}', style=tab_style, selected_style=tab_selected_style)
            for key,value in self.title_tab.items()
        ]
        
        self.app.layout = dbc.Container([
            dbc.Row(
                [
                    dbc.Col(html.Img(src=self.app.get_asset_url(self.icon_theme),style={"width":"65px","margin-left":"20px"}), width=3,style={"background-color": self.color_theme,"padding": "17px"}),
                    dbc.Col(
                        html.H1(self.title_general,style={"color":"white","margin-left":"20px"}
                    ), width=9,style={"background-color": self.color_theme,"padding": "15px"})
                ],
            ),

            dcc.Tabs(id='tabs-inline', value=list(self.title_tab.keys())[0], children=tabs_elements,style=tabs_styles,colors={
                "background": "white"
            }),

            html.Div(style={'margin': '40px'}),
            html.Div(id='tabs-example-content-1'),
            dcc.Download(id="download_df"),

        ],fluid=True)

    def run_server(self,port = 8053):
        self.app.run_server(debug=False,port=port)


       
    