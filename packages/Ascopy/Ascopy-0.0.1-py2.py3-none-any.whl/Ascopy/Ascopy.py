# version: 2023_09_14_17_27

import numpy as np
import pandas as pd
import copula
from scipy.optimize import minimize_scalar
from scipy.optimize import minimize
import stats_func as sf
from kde_diffusion import kde1d
from scipy.stats import norm
import matplotlib.pyplot as plt
from scipy import stats
from scipy.integrate import quad
import time
import os.path
from multiprocessing import cpu_count
from multiprocessing import Pool
from tqdm import tqdm
Number_of_threads=cpu_count()
copula_number = 22


    #************************************************************************
class Pilot():
    """ """ 
    u,v=0.0,0.0    
    def __init__(self, x, y, pdfs=None):            
        self.x=x
        self.y=y
        self.fitx_dic={}
        self.fity_dic={}     
        self.fname=sf.stats_fits()
        self.cname=sf.stats_cdfs()
        self.pname=sf.stats_pdfs()


        if pdfs is None:
            self.pdf_names=sf.pdf_common    ## list from stats_func.py 
        else:
            self.pdf_names=pdfs 

    def _lnlike(self, para):
        #print('****',para)
        ans = np.log( copula.copulas(self.u, self.v, para) )
        #print('#####',para)
        ans = -np.sum(ans)  
        #print('ans',ans)
        return  ans


    def copula_fit(self, copula_name, quiet=True):
        if copula_name==22:
            theta_min, theta_max = copula.set_value(copula_name)
            bound_theta=[(-0.999, 0.999),(1.0,1000)]
            x0=np.array([0.1,3.0])
            #try:
            res = minimize(self._lnlike, x0, method='Powell', bounds=bound_theta, options={'xtol': 1e-4, 'ftol': 1e-4, 'disp': False})
            theta=res.x
            #except:
            #    theta=None
            return theta   
        else:        
            theta_min, theta_max = copula.set_value(copula_name) 
            bound_theta=(theta_min, theta_max)
            try:
                res = minimize_scalar(self._lnlike, bounds=bound_theta, method='bounded')          
                theta=res.x
            except:
                theta=None
            if not quiet: 
                print('    bound for theta:  ', bound_theta)
                print('    Optimal theta:    ', '%.4f' % theta)              
            return theta 
        
 
    def cdf(self, x, method='norm'):
        num=len(x)
        ans=np.zeros(num)
#    test=mykde.Kde1d(sample=x,adaptive=False)    #################
#    if method == 'KDE':
#        test.get_optimal_h()
#        for i in range(num):
#            ans[i]=test.cdf(x[i])
        if method == 'norm':
            loc, scale = norm.fit(x)
            ans = norm.cdf(x=x, loc=loc, scale=scale)
        elif method == 'maxwell':
            loc, scale = stats.maxwell.fit(x)
            ans = stats.maxwell.cdf(x=x, loc=loc, scale=scale)
        elif method == 't':
            df, loc, scale = stats.t.fit(x)
            ans = stats.t.cdf(x=x, df=df, loc=loc, scale=scale)
        elif method == 'gamma':
            a, loc, scale = stats.gamma.fit(x)
            ans = stats.gamma.cdf(x=x, a=a, loc=loc, scale=scale)    
        else:
            print("The second argument","'",method,"'","is not valid.", "Valid input includes 'KDE','norm'." )    
        return ans      

    def cdf_all(self, x, method='norm'):
#        cname=sf.stats_cdfs()
#        fname=sf.stats_fits()
        
        fit = self.fname[method](x)
        if len(fit) == 2: 
            ans = self.cname[method](x, fit[0], fit[1])
        elif len(fit) == 3:    
            ans = self.cname[method](x, fit[0],fit[1],fit[2])
        elif len(fit) == 4:    
            ans = self.cname[method](x, fit[0],fit[1],fit[2],fit[3])
        elif len(fit) == 5:    
            ans = self.cname[method](x, fit[0],fit[1],fit[2],fit[3],fit[4])                                            
        else:
            print('check the pdf used!')         
            return   
        return ans
        

    def cdf_fit(self, x, method, fit):
#        cname=sf.stats_cdfs()       
        
        if len(fit) == 2: 
            ans = self.cname[method](x, fit[0], fit[1])
        elif len(fit) == 3:    
            ans = self.cname[method](x, fit[0],fit[1],fit[2])
        elif len(fit) == 4:    
            ans = self.cname[method](x, fit[0],fit[1],fit[2],fit[3])
        elif len(fit) == 5:    
            ans = self.cname[method](x, fit[0],fit[1],fit[2],fit[3],fit[4])                                            
        else:
            print('check the pdf used!')         
            return   
        return ans
            
    
    def marginal_pdf(self, x, hist_bins=20):
        fit_dict={} 
        best={}    
        ks_dict={}
        width=max(x)-min(x)
        x1 = min(x) - 0.15*width
        x2 = max(x) + 0.15*width    
        nd=200      
        grid = np.linspace(x1, x2, nd)
    
        ix=0
        try:    
            loc, scale = norm.fit(x)             
            density_norm = norm.pdf(x=grid, loc=loc, scale=scale)
            ks = stats.ks_1samp(x, stats.norm.cdf, args=(loc, scale))
            #print('fit to norm:     p_value =',ks[1])
            fit_dict["norm"] = np.array([loc,scale])
            ks_dict["norm"] = [ix, ks[1], density_norm]
            ix=ix+1
        except:
            print('The normal distribution can be rejected.')
        
        
        try:    
            loc, scale = stats.maxwell.fit(x)              
            density_maxwell = stats.maxwell.pdf(x=grid, loc=loc, scale=scale) 
            ks = stats.ks_1samp(x, stats.maxwell.cdf, args=(loc, scale))
            #print('fit to maxwell:  p_value =',ks[1])
            fit_dict["maxwell"] = np.array([loc,scale])
            ks_dict["maxwell"] = [ix, ks[1], density_maxwell]
            ix=ix+1        
        except:
            print('The maxwell distribution can be rejected.')        
    
        try:
            df, loc, scale = stats.t.fit(x)
            density_t = stats.t.pdf(x=grid, df=df, loc=loc, scale=scale)
            ks = stats.ks_1samp(x, stats.t.cdf, args=(df, loc, scale))
            #print('fit to t:        p_value =',ks[1])
            fit_dict["t"] = np.array([df,loc,scale])
            ks_dict["t"] = [ix, ks[1], density_t]
            ix=ix+1        
        except:
            print('The t distribution can be rejected.') 
   
        try:
            a, loc, scale = stats.gamma.fit(x)
            density_gamma = stats.gamma.pdf(x=grid, a=a, loc=loc, scale=scale)
            ks = stats.ks_1samp(x, stats.gamma.cdf, args=(a, loc, scale))
            #print('fit to gamma:    p_value =',ks[1])
            fit_dict["gamma"] = np.array([a,loc,scale])
            ks_dict["gamma"] = [ix, ks[1],  density_gamma]
            ix=ix+1        
        except:
            print('The gamma distribution can be rejected.')  
        
        try:    
            loc, scale = stats.gumbel_l.fit(x)              
            density_gumbel_l = stats.gumbel_l.pdf(x=grid, loc=loc, scale=scale) 
            ks = stats.ks_1samp(x, stats.gumbel_l.cdf, args=(loc, scale))
            #print('fit to gumbel_l:  p_value =',ks[1])
            fit_dict["gumbel_l"] = np.array([loc,scale])
            ks_dict["gumbel_l"] = [ix, ks[1], density_gumbel_l]
            ix=ix+1        
        except:
            print('The gumbel_l distribution can be rejected.') 
    
        try:
            K, loc, scale = stats.exponnorm.fit(x)
            density_exponnorm = stats.exponnorm.pdf(x=grid, K=K, loc=loc, scale=scale)
            ks = stats.ks_1samp(x, stats.exponnorm.cdf, args=(K, loc, scale))
            #print('fit to exponnorm:    p_value =',ks[1])
            fit_dict["exponnorm"] = np.array([K,loc,scale])
            ks_dict["exponnorm"] = [ix, ks[1],  density_exponnorm]
            ix=ix+1        
        except:
            print('The exponnorm distribution can be rejected.') 

        temp = np.zeros(ix)
        for keys in ks_dict:
            i = ks_dict[keys][0] 
            temp[i] = ks_dict[keys][1]    
        idx = np.argsort(temp)
    
        for keys in ks_dict:
            if ks_dict[keys][0] == idx[-1]:
                best["1st"] = keys, ks_dict[keys][1], ks_dict[keys][2]                                      
            if ks_dict[keys][0] == idx[-2]:
                best["2nd"] = keys, ks_dict[keys][1], ks_dict[keys][2]       
            if ks_dict[keys][0] == idx[-3]:
                best["3rd"] = keys, ks_dict[keys][1], ks_dict[keys][2]  

        find=False
        for keys in best:
            if best[keys][0]=='norm':
                find=True
        if find is False:
            best["3rd"] = 'norm', ks_dict["norm"][1], ks_dict["norm"][2]        

        n, b = np.histogram( x, bins=hist_bins, density=True )
        #n = gaussian_filter(n, smooth1d)
        x0 = np.array(list(zip(b[:-1], b[1:]))).flatten()
        y0 = np.array(list(zip(n, n))).flatten() 
        
        best["hist"] = x0,y0
        best["grid"] = grid          
        return best, fit_dict


    def marginal_all(self, x, try_more_pdfs=False, hist_bins=20):
        not_used=[]
        fit_dict={} 
        best={}    
        ks_dict={}
#        fname=sf.stats_fits()
#        cname=sf.stats_cdfs()
#        pname=sf.stats_pdfs()
        
        if try_more_pdfs is True:
            self.pdf_names = sf.pdf_names          ## list from stats_func        
        
        width=max(x)-min(x)
        x1 = min(x) - 0.15*width
        x2 = max(x) + 0.15*width    
        nd=200      
        grid = np.linspace(x1, x2, nd)
    
        ix=0
        for na in tqdm(self.pdf_names):
            try:    
                fit=self.fname[na](x)
                ks = stats.ks_1samp(x, self.cname[na], args=fit)
                fit_dict[na] = [fit, ks[1]]
                ks_dict[na] = [ix, ks[1]]
                #print(na,ks[1])
                ix=ix+1
            except:
                not_used.append(na)        
        
        temp = np.zeros(ix)
        for keys in ks_dict:
            i = ks_dict[keys][0] 
            temp[i] = ks_dict[keys][1]    
        idx = np.argsort(temp)    

        for keys in ks_dict:
            if ks_dict[keys][0] == idx[-1]:
                best_pdf1=keys                                                      
            if ks_dict[keys][0] == idx[-2]:
                best_pdf2=keys       
            if ks_dict[keys][0] == idx[-3]:
                best_pdf3=keys     
        best_pdf=[best_pdf1,best_pdf2,best_pdf3]
        best_idx=['1st','2nd','3rd']
        
        i=0
        for keys in best_pdf:
            fit,ks=fit_dict[keys]
            if len(fit) == 2: 
                density = self.pname[keys](grid, fit[0], fit[1])
            elif len(fit) == 3:    
                density = self.pname[keys](grid, fit[0],fit[1],fit[2])
            elif len(fit) == 4:    
                density = self.pname[keys](grid, fit[0],fit[1],fit[2],fit[3])
            elif len(fit) == 5:    
                density = self.pname[keys](grid, fit[0],fit[1],fit[2],fit[3],fit[4])                                            
            else:
                print('check the pdf used!')        
            best[best_idx[i]] = keys, ks_dict[keys][1], density
            i=i+1
        
        find=False
        for keys in best:
            if best[keys][0]=='norm':
                find=True
        if find is False:
            fit,ks=fit_dict["norm"]
            density = self.pname["norm"](grid, fit[0],fit[1])
            best["3rd"] = 'norm', ks_dict["norm"][1], density       

        n, b = np.histogram( x, bins=hist_bins, density=True )
        x0 = np.array(list(zip(b[:-1], b[1:]))).flatten()
        y0 = np.array(list(zip(n, n))).flatten() 
        
        best["hist"] = x0,y0
        best["grid"] = grid     
           
        return best, fit_dict


    def get_margins(self, try_more_pdfs=False, plot_KDE=True):        
        (density_kde1, grid_kde1, bandwidth1) = kde1d(self.x, n=1024)
        (density_kde2, grid_kde2, bandwidth2) = kde1d(self.y, n=1024)        
#        if try_more_pdfs:
        fitx, self.fitx_dic = self.marginal_all(self.x, try_more_pdfs)    
        fity, self.fity_dic = self.marginal_all(self.y, try_more_pdfs)
#        else:
#            fitx = self.marginal_pdf(self.x)  
#            fity = self.marginal_pdf(self.y)         
        
        gridx = fitx["grid"]   
        histx1,histx2 = fitx["hist"]
        gridy = fity["grid"]   
        histy1,histy2 = fity["hist"]        
        
        
        dispx = {}
        dispx['PDFs']=[fitx['1st'][0], fitx['2nd'][0], fitx['3rd'][0]]
        dispx['p_value']=[fitx['1st'][1], fitx['2nd'][1], fitx['3rd'][1]]
        dispy = {}
        dispy['PDFs']=[fity['1st'][0], fity['2nd'][0], fity['3rd'][0]]
        dispy['p_value']=[fity['1st'][1], fity['2nd'][1], fity['3rd'][1]]        
        
        print("fitting x:")
#        for keys in fitx:
#            if keys == "1st" or keys == "2nd" or keys == "3rd":
#                print("    fit to", "{:<10}".format(fitx[keys][0]+","), 'p_value=', '%.4f' %fitx[keys][1])
         
         
                 
        print(pd.DataFrame.from_dict(dispx)) 
         
            
        print("fitting y:")
        print(pd.DataFrame.from_dict(dispy)) 
#        for keys in fity:
#            if keys == "1st" or keys == "2nd" or keys == "3rd":
#                print("    fit to",  "{:<10}".format(fity[keys][0]+","), 'p_value=', '%.4f' %fity[keys][1])       
        
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 6),tight_layout=True, sharey=True)
        if plot_KDE:
            ax1.plot(grid_kde1, density_kde1, label="KDE", linestyle='--', linewidth=1, color='black', alpha=0.6)        
        ax1.plot(histx1, histx2, linestyle='-', color='black', alpha=0.5)
        ax1.plot(gridx, fitx["1st"][2],  label=fitx["1st"][0], linestyle='-.', linewidth=1, color='red', alpha=0.6)
        ax1.plot(gridx, fitx["2nd"][2],  label=fitx["2nd"][0], linestyle='-.', linewidth=1, color='green', alpha=0.6)
        ax1.plot(gridx, fitx["3rd"][2],  label=fitx["3rd"][0], linestyle='-.', linewidth=1, color='cyan', alpha=0.6)
        ax1.legend()
        if plot_KDE:
            ax2.plot(grid_kde2, density_kde2, label="KDE", linestyle='--', linewidth=1, color='black', alpha=0.6)        
        ax2.plot(histy1, histy2, linestyle='-', color='black', alpha=0.5)
        ax2.plot(gridy, fity["1st"][2],  label=fity["1st"][0], linestyle='-.', linewidth=1, color='red', alpha=0.6)
        ax2.plot(gridy, fity["2nd"][2],  label=fity["2nd"][0], linestyle='-.', linewidth=1, color='green', alpha=0.6)
        ax2.plot(gridy, fity["3rd"][2],  label=fity["3rd"][0], linestyle='-.', linewidth=1, color='cyan', alpha=0.6)
        ax2.legend()
        ax1.set_ylabel('PDF',fontsize=16)
        ax1.set_xlabel('x',fontsize=18)
        ax2.set_xlabel('y',fontsize=18)
        fig.suptitle('marginal PDFs')
        fig.autofmt_xdate()
        plt.show()         
        return

    def plot_margins(self, PDFx='norm', PDFy='norm', plot_KDE=True, hist_bins=20):        
#        fname=sf.stats_fits()
#        pname=sf.stats_pdfs()

        (density_kde1, grid_kde1, bandwidth1) = kde1d(self.x, n=1024)
        (density_kde2, grid_kde2, bandwidth2) = kde1d(self.y, n=1024)        
      
        n, b = np.histogram( self.x, bins=hist_bins, density=True )
        hx1 = np.array(list(zip(b[:-1], b[1:]))).flatten()
        hx2 = np.array(list(zip(n, n))).flatten() 
        n, b = np.histogram( self.y, bins=hist_bins, density=True )
        hy1 = np.array(list(zip(b[:-1], b[1:]))).flatten()
        hy2 = np.array(list(zip(n, n))).flatten() 
        
        
        width=max(self.x)-min(self.x)
        x1 = min(self.x) - 0.15*width
        x2 = max(self.x) + 0.15*width    
        nd=200      
        gridx = np.linspace(x1, x2, nd)        
        width=max(self.y)-min(self.y)
        y1 = min(self.y) - 0.15*width
        y2 = max(self.y) + 0.15*width         
        gridy = np.linspace(y1, y2, nd)

        fit=self.fname[PDFx](self.x)
        if len(fit) == 2: 
            density_x = self.pname[PDFx](gridx, fit[0], fit[1])
        elif len(fit) == 3:    
            density_x = self.pname[PDFx](gridx, fit[0],fit[1],fit[2])
        elif len(fit) == 4:    
            density_x = self.pname[PDFx](gridx, fit[0],fit[1],fit[2],fit[3])                                          
        else:
            print('check the PDFx used!') 

        fit=self.fname[PDFy](self.y)
        if len(fit) == 2: 
            density_y = self.pname[PDFy](gridy, fit[0], fit[1])
        elif len(fit) == 3:    
            density_y = self.pname[PDFy](gridy, fit[0],fit[1],fit[2])
        elif len(fit) == 4:    
            density_y = self.pname[PDFy](gridy, fit[0],fit[1],fit[2],fit[3])                                          
        else:
            print('check the PDFy used!')  
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 6),tight_layout=True, sharey=True)
        if plot_KDE:
            ax1.plot(grid_kde1, density_kde1, label="KDE", linestyle='--', linewidth=1, color='black', alpha=0.6)        
        ax1.plot(hx1, hx2, linestyle='-', color='black', alpha=0.5)
        ax1.plot(gridx, density_x,  label=PDFx, linestyle='-.', linewidth=1, color='red', alpha=0.6)

        ax1.legend()
        if plot_KDE:
            ax2.plot(grid_kde2, density_kde2, label="KDE", linestyle='--', linewidth=1, color='black', alpha=0.6)        
        ax2.plot(hy1, hy2, linestyle='-', color='black', alpha=0.5)
        ax2.plot(gridy, density_y,  label=PDFy, linestyle='-.', linewidth=1, color='red', alpha=0.6)

        ax2.legend()
        ax1.set_ylabel('PDF',fontsize=16)
        ax1.set_xlabel('x',fontsize=18)
        ax2.set_xlabel('y',fontsize=18)
        fig.suptitle('marginal PDFs')
        fig.autofmt_xdate()
        plt.show()         
        return

    def get_fit_all(self, max_row=50):
        Xpdfs={}
        Ypdfs={}
        col1=[]
        col2=[]
        col3=[]
        for aa in self.fitx_dic:
            col1.append(aa)
            col2.append(self.fitx_dic[aa][0])
            col3.append(self.fitx_dic[aa][1])
        idx = np.argsort(col3)[::-1]    
        col1n=[]
        col2n=[]
        col3n=[]
        num = min(len(col1),max_row)
        for i in range(num):
            col1n.append(col1[idx[i]])
            col2n.append(col2[idx[i]])
            col3n.append(col3[idx[i]])             
        Xpdfs['pdf']=col1n
        Xpdfs['fit']=col2n
        Xpdfs['p_value']=col3n
        
        col1=[]
        col2=[]
        col3=[]
        for aa in self.fity_dic:
            col1.append(aa)
            col2.append(self.fity_dic[aa][0])
            col3.append(self.fity_dic[aa][1])
        idx = np.argsort(col3)[::-1]    
        col1n=[]
        col2n=[]
        col3n=[]
        num = min(len(col1),max_row)
        for i in range(num):
            col1n.append(col1[idx[i]])
            col2n.append(col2[idx[i]])
            col3n.append(col3[idx[i]])             
        Ypdfs['pdf']=col1n
        Ypdfs['fit']=col2n
        Ypdfs['p_value']=col3n
        return Xpdfs,Ypdfs    

    def cpdf(self,y, Fx,theta,fy,PDFy):            
        self.judge=True                 ############&&&&&&&&&?????????????????????        
        F = Fx
        G=self.cdf_fit(x=y, method=PDFy, fit=fy)       
        if self.judge is True:
            ans = copula.copulae(F,G,theta)*self.pdf_fit(x=y, method=PDFy, fit=fy)
        else:
            ans = copula.copulae(F,G,theta)    
        return -ans


    def get_peak(self, PDFx='norm', PDFy='norm', copula_name=None, gridx=None, plot_fig=True, judge=True):                 
        self.judge=judge
        fx = self.fitx_dic[PDFx][0]
        fy = self.fity_dic[PDFy][0]        
        self.u=self.cdf_fit(self.x, method=PDFx, fit=fx)
        self.v=self.cdf_fit(self.y, method=PDFy, fit=fy)
        theta = self.copula_fit(copula_name=copula_name, quiet=True)
        print('theta',theta)
        if gridx is None:
            nmags = 50
            x1,x2=min(self.x),max(self.x)
            gridx=np.linspace(x1, x2, nmags)                
        pks=[]
        bound=(min(self.y), max(self.y))
        for m in gridx:        
            Fx = self.cdf_fit(x=m, method=PDFx, fit=fx)        
            res = minimize_scalar(self.cpdf, bounds=bound, method='bounded',args=(Fx,theta,fy,PDFy))
            pks.append(res.x)        
        
        if plot_fig:     
            fig = plt.figure(figsize=(8, 6), dpi=100)
            ax = fig.add_subplot(1, 1, 1)
            ax.tick_params('both', which='major', length=7, width=1)
            ax.tick_params('both', which='minor', length=3, width=1)             
            ax.plot(gridx, pks, lw=1.5, c='red', zorder=3, label='Copula peak')        
            plt.errorbar(self.x, self.y, fmt=".k", capsize=0, lw=1.0,ms=2.5,label='data', alpha=0.5)
            plt.ylabel(r'$y$',fontsize=18)
            plt.xlabel(r'$x$',fontsize=18)
            plt.legend();
            #plt.xlim(lmin, self.Lmax)
            #plt.ylim(y1,y2)
            plt.show()         
        return gridx,pks


    def find_copula(self,lp=None, pdfs=None,eps=1e-6):
        if pdfs is None:
            pdfs = self.pdf_names
        npa = sf.stats_npa()
        nc = 1                          #  parameter number of copula %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%       
        dic = {}
        pdfx = []
        pdfy = []        
        
        for pn in self.pdf_names:
            fit,ks = self.fitx_dic[pn]    
            if ks>eps:
                pdfx.append(pn)
            fit,ks = self.fity_dic[pn]
            if ks>eps:
                pdfy.append(pn)         
        
        for PDFx in tqdm(pdfx):
            nx = npa[PDFx]
            fx,ks = self.fitx_dic[PDFx]
            self.u=self.cdf_fit(self.x, method=PDFx, fit=fx)
            dic_sub={}
            for PDFy in pdfy:
                ny = npa[PDFy]
                fy,ks = self.fity_dic[PDFy]
                p_k = nc + nx + ny
                self.v=self.cdf_fit(self.y, method=PDFy, fit=fy)                
                AIC=np.zeros(copula_number)
                theta=np.zeros(copula_number)
                for i in range(copula_number): 
                    theta[i] = self.copula_fit(copula_name=i+1, quiet=True)                    
                    AIC[i] = 2*self._lnlike(theta[i]) + 2*p_k
                    if np.isnan(AIC[i]):
                        AIC[i]=np.inf
                #######################################################################
                if lp is not None:
                    idx=np.argsort(AIC)
                    for i in idx[0:3]:                    
                        copula_name = i+1
                        theta_min, theta_max = copula.set_value(copula_name)                    
                        pks=[]
                        bound=(min(self.y), max(self.y))
                        for m in lp[0]:        
                            Fx = self.cdf_fit(x=m, method=PDFx, fit=fx)        
                            res = minimize_scalar(self.cpdf, bounds=bound, method='bounded',args=(Fx,theta[i],fy,PDFy))
                            pks.append(res.x) 
                        sig = (lp[2]-lp[3])/2
                        ans=((pks-lp[1])/sig)**2
                        AIC[i] = AIC[i] + np.sum(ans)                                       
                    for i in idx[3:]:
                        AIC[i] = AIC[i] + np.inf               
                #######################################################################
                dic_sub[PDFy] = AIC              
            dic[PDFx] = dic_sub 
        
        #pdfx=['beta', 'betaprime', 'chi2', 'f', 'gamma']
        #pdfy=['alpha', 'beta', 'betaprime', 'chi', 'f', 'gamma', 'logistic', 'lognorm', 't']
        num = len(pdfx)*len(pdfy)*2
        aic_min = np.zeros(num)
        cnum = np.zeros(num)
        i=0
        nl = []
        for ni in pdfx:
            for nj in pdfy:
                idx = np.argsort(dic[ni][nj])        
                aic_min[i] = dic[ni][nj][idx[0]]
                cnum[i] = idx[0]+1
                nl.append((ni,nj))
                i=i+1
                aic_min[i] = dic[ni][nj][idx[1]]        
                cnum[i] = idx[1]+1        
                nl.append((ni,nj))
                i=i+1
        
        idx = np.argsort(aic_min) 
        dic_sort={}
        col1,col2,col3,col4=[],[],[],[]
        for i in idx[:50]:
        #print(nl[i],int(cnum[i]), aic_min[i])
            col1.append(nl[i][0])
            col2.append(nl[i][1])
            col3.append(int(cnum[i]))
            col4.append(aic_min[i])
    
        dic_sort['PDFx']=col1
        dic_sort['PDFy']=col2
        dic_sort['Copula number'] = col3
        dic_sort['AIC']=col4
        temp=pd.DataFrame.from_dict(dic_sort)
        print(temp)         
        return dic_sort
        
    
    def get_copula(self, PDFx='norm', PDFy='norm', copula_name=None):       
        ''' get copula '''
        self.u=self.cdf_all(self.x, method=PDFx)
        self.v=self.cdf_all(self.y, method=PDFy)
        npa = sf.stats_npa()
        if copula_name == 22:
            nc=2
        else:
            nc = 1                           #  parameter number of copula %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        nx = npa[PDFx]
        ny = npa[PDFy]
        p_k = nc + nx + ny
        
        if copula_name is None:            
            Num=copula_number
            AIC=np.zeros(Num)
            theta=np.zeros(Num)
            for i in range(Num): 
                theta[i] = self.copula_fit(copula_name=i+1, quiet=True) 
                #print('copula_name:',i+1,'theta=',theta[i])
                AIC[i] = 2*self._lnlike(theta[i]) + 2*p_k
                if np.isnan(AIC[i]):
                    AIC[i]=np.inf
            idx = np.argsort(AIC)
            print('the best five copulas are sorted as follows：')
            print('No.', "{:<2}".format(idx[0]+1),'copula:','AIC=', '%.4f' %AIC[idx[0]], ",", 'theta=', '%.4f' %theta[idx[0]])
            print('No.', "{:<2}".format(idx[1]+1),'copula:','AIC=', '%.4f' %AIC[idx[1]], ",", 'theta=', '%.4f' %theta[idx[1]])
            print('No.', "{:<2}".format(idx[2]+1),'copula:','AIC=', '%.4f' %AIC[idx[2]], ",", 'theta=', '%.4f' %theta[idx[2]])
            print('No.', "{:<2}".format(idx[3]+1),'copula:','AIC=', '%.4f' %AIC[idx[3]], ",", 'theta=', '%.4f' %theta[idx[3]])
            print('No.', "{:<2}".format(idx[4]+1),'copula:','AIC=', '%.4f' %AIC[idx[4]], ",", 'theta=', '%.4f' %theta[idx[4]])
            #print('No.',idx[5]+1,'copula:','AIC=',AIC[idx[4]], 'theta=', '%.4f' %theta[idx[5]])
            #print('No.',idx[6]+1,'copula:','AIC=',AIC[idx[4]], 'theta=', '%.4f' %theta[idx[6]])
            cn = np.array([idx[0],idx[1],idx[2],idx[3],idx[4]]) +1
            aic =np.array([AIC[idx[0]], AIC[idx[1]], AIC[idx[2]], AIC[idx[3]], AIC[idx[4]]])  
            return [cn,aic]
        else:            
            theta = self.copula_fit(copula_name=copula_name)    
            #print('***********************here***********************')
            print(theta)
            AIC = 2*self._lnlike(theta) + 2*p_k
            if nc==1:
                print('No.',"{:<2}".format(copula_name),'copula:','AIC=', '%.4f' %AIC, ",", 'theta=', '%.4f' %theta)            
            else:
                print('No.',"{:<2}".format(copula_name),'copula:','AIC=', '%.4f' %AIC, ",", 'theta=', theta)


    def pdf_fit(self, x, method, fit):
#        pname=sf.stats_pdfs()       
        
        if len(fit) == 2: 
            ans = self.pname[method](x, fit[0], fit[1])
        elif len(fit) == 3:    
            ans = self.pname[method](x, fit[0],fit[1],fit[2])
        elif len(fit) == 4:    
            ans = self.pname[method](x, fit[0],fit[1],fit[2],fit[3])
        elif len(fit) == 5:    
            ans = self.pname[method](x, fit[0],fit[1],fit[2],fit[3],fit[4])                                            
        else:
            print('check the pdf used!')         
            return   
        return ans





################################################################################################
################################################################################################


################################################################################################
################################################################################################


class Copula():
    """ """ 
    u,v=0.0,0.0
    mcmc_fit, ml_fit=0.0, 0.0
    mcmc_fit_done, ml_fit_done = False, False
    data_loaded=False
    like_num=3
    user_defined_xcdf,user_defined_xpdf,user_defined_ycdf,user_defined_ypdf = False, False, False, False
    
    def __init__(self, x, y, copula_num, PDFx, PDFy, CDFx=None, CDFy=None, nc=1, nx=None, ny=None):            
        
        ####    &&&&&&&&&&&&&&&&&&&&&&& ????????  what about when nc=2 ??
        
        self.x = x
        self.y = y
        self.copula_num = copula_num
        self.PDFx = PDFx    
        self.PDFy = PDFy                             
        self.CDFx = CDFx
        self.CDFy = CDFy
        self.nx = nx
        self.ny = ny
        self.nc = nc
        self.ndim = 0                #self.nx + self.ny + self.nc
        self.h_lower = 0.0           #np.zeros(self.ndim)
        self.h_upper = 0.0           #np.zeros(self.ndim)
        self.pdf_names=sf.pdf_names       

        if self.copula_num == 22:              ######????????????????
            self.nc = 2        
        
        if callable(self.PDFx) or callable(self.CDFx):
            if self.nx is None:
                print("The argument 'nx' is missing for Copula()!")
                return
        
        if callable(self.PDFy) or callable(self.CDFy):
            if self.ny is None:
                print("The argument 'ny' is missing for Copula()!")
                return
        
#    def __call__(self, x, theta):   
#        return self.xpdf(x, theta)
#        
#    def __call__(self, x, theta):   
#        return self.ypdf(x, theta) 
#        
#    def __call__(self, x, theta):   
#        return self.xcdf(x, theta)
#        
#    def __call__(self, x, theta):   
#        return self.ycdf(x, theta) 

    def initialize(self): 
        cname = sf.stats_cdfs()
        pname = sf.stats_pdfs()
        npa = sf.stats_npa()
        self.dic = {}
        
        if isinstance(self.PDFx, str):
            if self.PDFx in self.pdf_names:
                self.dic['xpdf'] = pname[self.PDFx]
                self.nx = npa[self.PDFx]
                self.CDFx = self.PDFx
            else:
                print('please check the argument PDFx!')
                return
        elif callable(self.PDFx):
            self.user_defined_xpdf = True
        else:
            print('please check the argument PDFx!')
            return        
        
        if isinstance(self.PDFy, str):
            if self.PDFy in self.pdf_names:
                self.dic['ypdf'] = pname[self.PDFy]
                self.ny = npa[self.PDFy]
                self.CDFy = self.PDFy
            else:
                print('please check the argument PDFy!')
                return
        elif callable(self.PDFy):
            self.user_defined_ypdf = True
        else:
            print('please check the argument PDFy!')
            return                                                
                    
        if isinstance(self.CDFx, str):            
            if self.CDFx in self.pdf_names:
                self.dic['xcdf'] = cname[self.CDFx]                    
            else:
                print('please check the argument CDFx!')
                return
        elif callable(self.CDFx):
            self.user_defined_xcdf = True
        else:
            print('please check the argument CDFx!')
            return                    

        if isinstance(self.CDFy, str):
            if self.CDFy in self.pdf_names:
                self.dic['ycdf'] = cname[self.CDFy]
            else:
                print('please check the argument CDFy!')
                return
        elif callable(self.CDFy):
            self.user_defined_ycdf = True
        else:
            print('please check the argument CDFy!')
            return                     
        
        self.ndim = self.nx + self.ny + self.nc
        self.h_lower = np.zeros(self.ndim)
        self.h_upper = np.zeros(self.ndim)        
        ans = copula.set_value(self.copula_num)
        self.data_loaded = True          
        return ans  
        
  
    #************************************************************************    
    def xpdf(self, x, theta):
        if self.user_defined_xpdf:
            ans = self.PDFx(x, theta)        
        else:  
            if self.nx == 2:
                ans  = self.dic['xpdf'](x, theta[0],theta[1])
            elif self.nx == 3:
                ans  = self.dic['xpdf'](x, theta[0],theta[1],theta[2])
            elif self.nx == 4:
                ans  = self.dic['xpdf'](x, theta[0],theta[1],theta[2],theta[3])
        return ans
    
    def xcdf(self, x, theta):
        if self.user_defined_xcdf: 
            ans = self.CDFx(x, theta)
        else:
            if self.nx == 2:
                ans  = self.dic['xcdf'](x, theta[0],theta[1])
            elif self.nx == 3:
                ans  = self.dic['xcdf'](x, theta[0],theta[1],theta[2])
            elif self.nx == 4:
                ans  = self.dic['xcdf'](x, theta[0],theta[1],theta[2],theta[3])             
        return ans    
    
    def ypdf(self, y, theta):
        if self.user_defined_ypdf: 
            ans = self.PDFy(y, theta)
        else:    
            if self.ny == 2:
                ans  = self.dic['ypdf'](y, theta[0],theta[1])
            elif self.ny == 3:
                ans  = self.dic['ypdf'](y, theta[0],theta[1],theta[2])
            elif self.ny == 4:
                ans  = self.dic['ypdf'](y, theta[0],theta[1],theta[2],theta[3])             
        return ans
        
    def ycdf(self, y, theta):
        if self.user_defined_ycdf: 
            ans = self.CDFy(y, theta)
        else:    
            if self.ny == 2:
                ans  = self.dic['ycdf'](y, theta[0],theta[1])
            elif self.ny == 3:
                ans  = self.dic['ycdf'](y, theta[0],theta[1],theta[2])
            elif self.ny == 4:
                ans  = self.dic['ycdf'](y, theta[0],theta[1],theta[2],theta[3])            
        return ans       
    
  
    def log_likex(self, para):
        ans = np.log( self.xpdf(self.x, para) )
        return  np.sum(ans)
        
    def log_likey(self, para):
        ans = np.log( self.ypdf(self.y, para) )
        return  np.sum(ans)         
        
    def log_likec(self, para):
        ans = np.log( copula.copulas(self.u, self.v, para) )
        return  np.sum(ans)

    
    def log_like(self, para):
        #print(para)
        if self.nc==1:
            theta = para[0]
        else:
            theta = para[0:self.nc]
        px = para[self.nc:self.nc+self.nx]    
        py = para[self.nc+self.nx:]
        u = self.xcdf(self.x, px)
        v = self.ycdf(self.y, py)        
        cop = copula.copulas(u,v,theta)
        ans = np.log(cop) + np.log( self.xpdf(self.x, px) ) + np.log( self.ypdf(self.y, py) )    
        return np.sum(ans)  
    

    def _lnlike(self,theta): 
        if self.like_num==1:
            return -self.log_likex(theta)
        elif self.like_num==2:
            return -self.log_likey(theta)
        elif self.like_num==3:
            return -self.log_likec(theta)
        else:
            return -self.log_like(theta)    

    def AIC(self, para):        
        if self.nc==1:
            theta = para[0]
        else:
            theta = para[0:self.nc]
        px = para[self.nc:self.nc+self.nx]    
        py = para[self.nc+self.nx:]
        u = self.xcdf(self.x, px)
        v = self.ycdf(self.y, py)        
        cop = np.log( copula.copulas(u,v,theta) )
        ans = -2*np.sum(cop) + 2*self.ndim 
        return ans


    ##################################################################################################################################
            
    def log_prior(self,theta):        
        if np.all(theta > self.h_lower) and np.all(theta < self.h_upper):        
            return 0.0
        return -np.inf          


    def lnprob(self, theta):
        lp = self.log_prior(theta)
        if not np.isfinite(lp):
            return -np.inf
        return lp + self.log_like(theta) 
        
    ###%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    ###%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  

    

    ##################################################################################################################################

    
    def get_ml_fit(self, x0=None, y0=None, xbound=None, ybound=None, one_step_fit=False):                 
        theta_min,theta_max = self.initialize()   
        #print('theta_min,theta_max',theta_min,theta_max)
        fname = sf.stats_fits()
        if self.user_defined_xpdf is False:
            x0 = fname[self.PDFx](self.x)
            print('x0',x0)
        if self.user_defined_xpdf is True:
            if x0 is None or xbound is None:
                print("The arguments 'x0' and 'xbound' are missing for get_ml_fit()!")
                return        
 
        if self.user_defined_ypdf is False:
            y0 = fname[self.PDFy](self.y)
            print('y0',y0)
        if self.user_defined_ypdf is True:
            if y0 is None or ybound is None:
                print("The arguments 'y0' and 'ybound' are missing for get_ml_fit()!")
                return 
                     
        self.like_num=1
        if xbound is None:
            res = minimize(self._lnlike, x0)  
        else:            
            #if not self.quiet:
            #    print('    bounds for parameters:  ',self.parameter_bound)
            res = minimize(self._lnlike, x0, method='Powell', bounds=xbound, options={'xtol': 1e-4, 'ftol': 1e-4, 'disp': False})            
        thetax=res.x
        print('Maximum likelihood estimation fit for xpdf:')
        for th in thetax: 
            print('%.6f' % th)         
        for i in range(self.nx):
            if thetax[i]>0.0:
                self.h_lower[self.nc+i], self.h_upper[self.nc+i] = thetax[i]/5, thetax[i]*2    
            else:
                self.h_lower[self.nc+i], self.h_upper[self.nc+i] = thetax[i]*2, thetax[i]/5     
        
        
        self.like_num=2
        if ybound is None:
            res = minimize(self._lnlike, y0)  
        else:            
            #if not self.quiet:
            #    print('    bounds for parameters:  ',self.parameter_bound)
            res = minimize(self._lnlike, y0, method='Powell', bounds=ybound, options={'xtol': 1e-4, 'ftol': 1e-4, 'disp': False})            
        thetay=res.x
        print('Maximum likelihood estimation fit for ypdf:')
        for th in thetay: 
            print('%.6f' % th)       
        for i in range(self.ny):
            if thetay[i]>0.0:
                self.h_lower[self.nc+self.nx+i], self.h_upper[self.nc+self.nx+i] = thetay[i]/5, thetay[i]*2    
            else:
                self.h_lower[self.nc+self.nx+i], self.h_upper[self.nc+self.nx+i] = thetay[i]*2, thetay[i]/5       
        
        self.like_num=3
        self.u = self.xcdf(self.x, thetax)
        self.v = self.ycdf(self.y, thetay)
        
        if self.copula_num == 22:
            bound_theta=[(-0.999,0.999),(1.0,1000)]
            x0=[0.0,2.0]
            res = minimize(self._lnlike, x0, method='Powell', bounds=bound_theta, options={'xtol': 1e-4, 'ftol': 1e-4, 'disp': False})
            thetac=res.x   
        else:        
            res = minimize_scalar(self._lnlike, bounds=(theta_min,theta_max), method='bounded')
            thetac=res.x        
       
        print('Maximum likelihood estimation fit for copula:')
        if self.nc == 1:
            print('%.6f' % thetac)        
            if thetac>0.0:
                self.h_lower[0], self.h_upper[0] = max(thetac/3,theta_min), min(thetac*2,theta_max)    
            else:
                self.h_lower[0], self.h_upper[0] = max(thetac*3,theta_min), min(thetac/3,theta_max)
            self.h_lower[0], self.h_upper[0] = theta_min, theta_max              #  ??????????????????????????       
            thetac=np.array([thetac])
        else:
            self.h_lower[0], self.h_upper[0] = theta_min, theta_max               #  ??????????????????????????
            self.h_lower[1], self.h_upper[1] = thetac[1]/3, thetac[1]*3           #  ??????????????????????????
        
        self.ml_fit = np.concatenate((thetac,thetax,thetay))
        
        #############################################3
        if one_step_fit is True:
            self.like_num=0
            bound=[]
            for i in range(self.ndim):
                bound.append((self.h_lower[i], self.h_upper[i]))
            theta0=[]        
            theta0.append(thetac)
            for i in range(self.nx):
                theta0.append(thetax[i])
            for i in range(self.ny):
                theta0.append(thetay[i]) 

            print('bound')
            print(bound)
            print(theta0)
        
            res = minimize(self._lnlike, theta0, method='Powell', bounds=bound, options={'xtol': 1e-4, 'ftol': 1e-4, 'disp': False})            
            theta=res.x
            print('Maximum likelihood estimation fit:')
            for th in theta: 
                print('%.6f' % th)          
              
            self.ml_fit=res.x
        self.ml_fit_done=True
        return self.ml_fit   
              

    ###%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    ###%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
       
    
    def run_mcmc(self, chain_name=None, max_n=5000, Ntau=50, theta_bound=None, parallel=True, processes=None, chain_analysis=True):
        #import os.path
        import time
        import emcee
                        
        if processes is None:
            processes = Number_of_threads - 2      
        if parallel:            
            print("Number of threads used in parallel computing: {0}".format(processes))        
        
        ti=time.localtime(time.time())
        tim = str(ti.tm_year) + "_" + str(ti.tm_mon) + "_" + str(ti.tm_mday) + "_" + str(ti.tm_hour) + "_" + str(ti.tm_min)
                
        # Set up the backend
        # Don't forget to clear it in case the file already exists
        
        if chain_name is None:
            if isinstance(self.PDFx,str) and isinstance(self.PDFy,str):
                chain_name = "chain_" + self.PDFx + "_" + self.PDFy + "_" + 'copula_' + str(self.copula_num) + ".h5"
            else:
                chain_name = "chain_copula_" + str(self.copula_num) + ".h5"      
        else: 
            if not isinstance(chain_name,str):
                print("'chain_name' should be a string like 'name.h5'")
                return 
        
        
        if os.path.isfile(chain_name):
            print("The file '",chain_name,"' already exists, please clear or rename it before run a new MCMC!" )
            return
                
        if self.ml_fit_done is False:
            print('Maximum likelihood estimation not done. It starts now...')             
            self.get_ml_fit()
        ndim=self.ndim        
        
        if theta_bound is not None:
            try:
                self.h_lower[0], self.h_upper[0] = theta_bound   
            except:
                print('The argument theta_bound should be a tuple or list, e.g, (-0.1,0.1) or [-0.1,0.1]') 
                return   
        
        # Initialize the walkers
        npara=len(self.ml_fit)         
        pos = self.ml_fit + 1e-4 * np.random.randn(32, npara)  
        nwalkers, ndim = pos.shape
        backend = emcee.backends.HDFBackend(chain_name)
        backend.reset(nwalkers, ndim)
    
        # Initialize the sampler
        if parallel is True:                   
            #from multiprocessing import Pool
            os.environ["OMP_NUM_THREADS"] = "1"            
            with Pool(processes=processes) as pool:                
                sampler = emcee.EnsembleSampler(nwalkers, ndim, self.lnprob, backend=backend, pool=pool) 
        
                index = 0
                autocorr = np.empty(max_n)
    
                # This will be useful to testing convergence
                old_tau = np.inf     
                # Now we'll sample for up to max_n steps
                for sample in sampler.sample(pos, iterations=max_n, progress=True):
                    # Only check convergence every 50 steps
        
                    its=sampler.iteration
#                    if its % 50 == 0:
#                        f = open(logfilename, "a")
#                        print('completed:', its,"/",max_n, ',', 'progress:','%.2f' % (its/max_n*100),"%",file=f)
#                        f.close()   
                    if sampler.iteration % 50:
                        continue
    
                    # Compute the autocorrelation time so far
                    # Using tol=0 means that we'll always get an estimate even
                    # if it isn't trustworthy
                    tau = sampler.get_autocorr_time(tol=0)
                    autocorr[index] = np.mean(tau)
                    index += 1
    
                    # Check convergence
                    converged = np.all(tau * Ntau < sampler.iteration)
                    converged &= np.all(np.abs(old_tau - tau) / tau < 0.01)
                    if converged:
                        break
                    old_tau = tau        
        else:        
            sampler = emcee.EnsembleSampler(nwalkers, ndim, self.lnprob, backend=backend)    
            # We'll track how the average autocorrelation time estimate changes
            index = 0
            autocorr = np.empty(max_n)
    
            # This will be useful to testing convergence
            old_tau = np.inf     
            # Now we'll sample for up to max_n steps
            for sample in sampler.sample(pos, iterations=max_n, progress=True):
                # Only check convergence every 50 steps
        
                its=sampler.iteration
#                if its % 50 == 0:
#                    f = open(logfilename, "a")
#                    print('completed:', its,"/",max_n, ',', 'progress:','%.2f' % (its/max_n*100),"%",file=f)
#                    f.close()   
                if sampler.iteration % 50:
                    continue
    
                # Compute the autocorrelation time so far
                # Using tol=0 means that we'll always get an estimate even
                # if it isn't trustworthy
                tau = sampler.get_autocorr_time(tol=0)
                autocorr[index] = np.mean(tau)
                index += 1
    
                # Check convergence
                converged = np.all(tau * Ntau < sampler.iteration)
                converged &= np.all(np.abs(old_tau - tau) / tau < 0.01)
                if converged:
                    break
                old_tau = tau         
    
        n = 50 * np.arange(1, index + 1)
        y = autocorr[:index]
        
        plt.figure(figsize=(6, 5)) 
        ax=plt.axes([0.13,0.1, 0.82, 0.85])
        ax.tick_params(direction='in', top=True, right=True, labelsize=12)         
        plt.plot(n, n / float(Ntau), "--k", label=r"$\tau = N/$"+str(Ntau))
        plt.plot(n, y, "o-", label=r"$\tau = \hat{\tau}(N)$")
        plt.xlim(0, n.max())
        plt.ylim(0, y.max() + 0.1 * (y.max() - y.min()))
        plt.xlabel("number of samples, $N$", fontsize=15)
        plt.ylabel(r"mean $\hat{\tau}$", fontsize=15);        
        plt.legend(fontsize=12); 

        fig_name = "tau"  + tim + ".png"
        #plt.savefig(fig_name)
        
        if chain_analysis is True:
            self.chain_analysis(chain_name, plot_walkers=False)
        return
        
    ##############################################################################
    def chain_analysis ( self,chain_name, plot_walkers=False, labels = None):               
        # labels = [r"$\theta$", r"$\mu_{1}$", r"$\sigma_{1}$", r"$\mu_{2}$", r"$\sigma_{2}$"]
        # labs = ['theta', mu1, sigma1, mu2, sigma2]
        import emcee        

        if os.path.isfile(chain_name) is False:
            print("The file '",chain_name,"' does not exist, please check the file name and path!" )
            return
            
        reader = emcee.backends.HDFBackend(chain_name)

        ndim=self.ndim       
        if labels is None:
            lab_list1 = [r"$\theta_{11}$", r"$\theta_{12}$", r"$\theta_{13}$", r"$\theta_{14}$", r"$\theta_{15}$", r"$\theta_{16}$", r"$\theta_{17}$", r"$\theta_{18}$"]    
            lab_list2 = [r"$\theta_{21}$", r"$\theta_{22}$", r"$\theta_{23}$", r"$\theta_{24}$", r"$\theta_{25}$", r"$\theta_{26}$", r"$\theta_{27}$", r"$\theta_{28}$"] 
            labels=[]
            labs=[]
            if self.nc==1:
                labels.append( r"$\theta$" )
                labs.append('theta')
            elif self.nc==2:
                labels.append( r"$\theta_{01}$" )
                labels.append( r"$\theta_{02}$" ) 
                labs.append('theta01')
                labs.append('theta02')
                           
            for i in range(self.nx):
                labels.append(lab_list1[i])                
            for i in range(self.ny):
                labels.append(lab_list2[i])        
        lab_list1 = ['theta11', 'theta12','theta13','theta14','theta15','theta16','theta17','theta18']    
        lab_list2 = ['theta21', 'theta22','theta23','theta24','theta25','theta26','theta27','theta28'] 
        for i in range(self.nx):
            labs.append(lab_list1[i])                
        for i in range(self.ny):
            labs.append(lab_list2[i])       
        
        
        samples = reader.get_chain()
        if plot_walkers is True:
            fig, axes = plt.subplots(ndim, figsize=(10, 7), sharex=True)                     
            for i in range(ndim):
                ax = axes[i]            
                ax.plot(samples[:, :, i], "k", alpha=0.3)   
                ax.set_xlim(0, len(samples))
                ax.set_ylabel(labels[i])
                ax.yaxis.set_label_coords(-0.1, 0.5)
            axes[-1].set_xlabel("step number");

            fig_name = "walkers" + ".png"
            fig.savefig(fig_name)

        try:
            tau = reader.get_autocorr_time()
            burnin = int(2 * np.max(tau))
            thin = int(0.5 * np.min(tau))
            flat_samples = reader.get_chain(discard=burnin, flat=True, thin=thin)
            log_prob_samples = reader.get_log_prob(discard=burnin, flat=True, thin=thin)        
            print("burn-in: {0}".format(burnin))
            print("thin: {0}".format(thin))
            print("flat chain shape: {0}".format(flat_samples.shape))
            print("flat log prob shape: {0}".format(log_prob_samples.shape))       
            dis=max(200,burnin*1.5)
            dis=int(dis)
            goodchain=True
        except:
            print("WARNING: The chain is shorter than 50 times the integrated autocorrelation time for", ndim, "parameter(s). Use this estimate with caution and run a longer chain!")
            dis=200
            goodchain=False            
        self.samples=samples[dis:,:,:].reshape((-1, ndim))            
        
        import corner
        figure = corner.corner(self.samples, labels=labels,
                       quantiles=[0.16, 0.5, 0.84],
                       show_titles=True, title_fmt='.3f', title_kwargs={"fontsize": 12}) 


        fig_name = "triangle" + ".png"
        #figure.savefig(fig_name)        
       
        
        #from IPython.display import display, Math                                
        self.mcmc_fit=np.zeros(ndim)
        print(' ')
        print('********** MCMC bestfit and 1 sigma errors **********')        
        for i in range(ndim):
            mcmc = np.percentile(self.samples[:, i], [16, 50, 84])
            q = np.diff(mcmc)
            txt = "\mathrm{{{3}}} = {0:.3f}_{{-{1:.3f}}}^{{{2:.3f}}}"
            txt = txt.format(mcmc[1], q[0], q[1], labels[i])            
            print(labs[i], '=','%.4f' %mcmc[1], '-', '%.4f' %q[0], '+', '%.4f' %q[1])
            #display(Math(txt))
            self.mcmc_fit[i]=mcmc[1]
        print(' ')    
        self.mcmc_fit_done=True        
        AIC=self.AIC(self.mcmc_fit)
        print("AIC=",'%.4f' % AIC)        
        
        if goodchain is True:
            self.samples=flat_samples                                
        #print('self.samples',self.samples.shape)
        return 
###############################################################################

    def xpdf_post(self, mag, theta):          
        thetax = theta[self.nc:self.nc+self.nx]        
        phi= self.xpdf(mag, thetax)
#        phi=[]
#        for m in mag:
#            lfi = self.xpdf(m, thetax)
#            phi.append(lfi) 
        return phi

    def ypdf_post(self, mag, theta):   
        thetay = theta[self.nc+self.nx:]         
        phi= self.ypdf(mag, thetay)
#        phi=[]
#        for m in mag:
#            lfi = self.ypdf(m, thetay)
#            phi.append(lfi) 
        return phi        

    def cpdf(self,y, m):
        global theta
        thetac = theta[0:self.nc]                          ##################????????????????????????
        px = theta[self.nc:self.nc+self.nx]    
        py = theta[self.nc+self.nx:]        
        #F=self.xcdf(x, px)
        F=m
        G=self.ycdf(y, py)        
        ans = copula.copulas(F,G,thetac)*self.ypdf(y, py)
        return ans
      
    def f(self,y , m):
        return self.cpdf(y, m)*y      


    def g(self, mag):
        lfi,err = quad(self.f, self.y1, self.y2, args=(mag))
        return lfi


    def cpdf_post(self, mag, para):        
        global theta
        theta = para
        px = theta[self.nc:self.nc+self.nx]
        mags = self.xcdf(mag, px)
        #if __name__ == '__main__':
        with Pool() as pool:
            phi = pool.map(self.g, mags)
            
#        phi=[]
#        for m in mags:
#            phi.append(self.g(m))         
        return phi



    def plot_posterior(self, sigma=1,dpi=(100,2500), plot_fig=True, progress_bar=True):
        
        #from tqdm import tqdm
        if self.data_loaded is False:
            self.initialize() 
        
        nmags,nsample = min(dpi),max(dpi)        
        if nmags<=20 or nsample<=800:
            print("WARNING: the 'dpi' ",dpi, "is too small,", "Use this estimate with caution and run a larger dpi!")
            print("suggested dpi=(m, n) with m>40 and n>1000.")

        (density_x, grid_x, bandwidth_x) = kde1d(self.x, n=1024)
        (density_y, grid_y, bandwidth_y) = kde1d(self.y, n=1024) 
        
        nmags=max(50,nmags)        
        nsample=max(800,nsample)
        nmags=min(500,nmags)
        nsample=min(8000,nsample)          
        magsx=np.linspace(grid_x[0],grid_x[-1],nmags)
        magsy=np.linspace(grid_y[0],grid_y[-1],nmags)
        nsample = min(nsample,len(self.samples))        
        rsample = self.samples[np.random.randint(len(self.samples), size=nsample)]
        phix = np.zeros((nsample, nmags)) 
        phiy = np.zeros((nsample, nmags))       
        
        #bf = np.median(self.samples, axis=0)
        if self.mcmc_fit_done is True:        
            bf = self.mcmc_fit                         # bf is best fit by MCMC
            #print('bestfit MCMC',bf)        
        else:
            print("The subroutine 'chain_analysis()' should be executed!") 
        if progress_bar is True:            
            for i, theta in enumerate(tqdm(rsample)):                 
                phix[i] = self.xpdf_post(magsx,theta) 
                phiy[i] = self.ypdf_post(magsy,theta)             
        else:
            for i, theta in enumerate(rsample): 
                phix[i] = self.xpdf_post(magsx,theta) 
                phiy[i] = self.ypdf_post(magsy,theta)
                                        
        phi_fitx = self.xpdf_post(magsx,bf)
        phi_fity = self.ypdf_post(magsy,bf) 
            #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
            
        if sigma==1:        
            up_x = np.percentile(phix, 15.87, axis=0)       
            down_x = np.percentile(phix, 84.13, axis=0)   
            up_y = np.percentile(phiy, 15.87, axis=0)       
            down_y = np.percentile(phiy, 84.13, axis=0)        
        
        
        if sigma==3:
            up_x = np.percentile(phix, 0.135, axis=0)         
            down_x = np.percentile(phix, 99.865, axis=0)
            up_y = np.percentile(phiy, 0.135, axis=0)         
            down_y = np.percentile(phiy, 99.865, axis=0)             
        
        if plot_fig:            
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 6),tight_layout=True, sharey=True)
            ax1.plot(grid_x, density_x, label="KDE", linestyle='--', linewidth=1, color='green')
            if isinstance(self.PDFx, str):
                labx = self.PDFx
            else:
                labx = 'user defined PDFx'
            if isinstance(self.PDFy, str):
                laby = self.PDFy
            else:
                laby = 'user defined PDFy'                    
            ax1.plot(magsx, phi_fitx, label=labx, linestyle='-', linewidth=1, color='red')
            ax1.fill_between(magsx, down_x, y2=up_x, color='orange', alpha=0.4)
            ax1.legend()
            ax2.plot(grid_y, density_y, label="KDE", linestyle='--', linewidth=1, color='green')
            ax2.plot(magsy, phi_fity, label=laby, linestyle='-', linewidth=1, color='red')
            ax2.fill_between(magsy, down_y, y2=up_y, color='orange', alpha=0.4)
            ax2.legend()
            ax1.set_ylabel('PDF',fontsize=16)
            ax1.set_xlabel('x',fontsize=18)
            ax2.set_xlabel('y',fontsize=18)
            fig.suptitle('marginal PDFs')
            fig.autofmt_xdate()
            plt.show()
            
        result1=np.array([magsx,phi_fitx,down_x,up_x])
        result2=np.array([magsy,phi_fity,down_y,up_y])
        return (result1,result2)      
           
        
    def plot_regress(self, sigma=1,dpi=(50,1000), xlim=None, plot_fig=True, progress_bar=True):
        
        #from tqdm import tqdm
        if self.data_loaded is False:
            temp = self.initialize() 
        
        nmags,nsample = min(dpi),max(dpi)        
        if nmags<=20 or nsample<=800:
            print("WARNING: the 'dpi' ",dpi, "is too small,", "Use this estimate with caution and run a larger dpi!")
            print("suggested dpi=(m, n) with m>40 and n>1000.")        
        
#        nmags=max(50,nmags)        
#        nsample=max(800,nsample)
#        nmags=min(500,nmags)
#        nsample=min(8000,nsample)         
        
        lens=max(self.y)-min(self.y)
        self.y1 = min(self.y)-0.25*lens
        self.y2 = max(self.y)+0.25*lens        
        if xlim is None:
            x1 = min(self.x) - 0.05* ( max(self.x)-min(self.x) ) 
            x2 = max(self.x) + 0.05* ( max(self.x)-min(self.x) ) 
        else:
            try:
                x1=xlim[0]
                x2=xlim[1]
            except:
                print("xlim should be a tuple such as (1.0, 2.0)!")
                return                   
        mags=np.linspace(x1, x2,nmags)

        nsample = min(nsample,len(self.samples))        
        rsample = self.samples[np.random.randint(len(self.samples), size=nsample)]
        phi = np.zeros((nsample, nmags)) 
        
        
        #bf = np.median(self.samples, axis=0)
        if self.mcmc_fit_done is True:        
            bf = self.mcmc_fit                         # bf is best fit by MCMC
            #print('bestfit MCMC',bf)        
        else:
            print("The subroutine 'chain_analysis()' should be executed!") 

        phi_fit = self.cpdf_post(mags,bf)        
        
#        print('phi_fit')
#        print(phi_fit)
#        print(mags)
#        result=np.array([mags,phi_fit,phi_fit,phi_fit])
#        return result

        if progress_bar is True:            
            for i, theta in enumerate(tqdm(rsample)):                 
                phi[i] = self.cpdf_post(mags,theta) 
           
        else:
            for i, theta in enumerate(rsample): 
                phi[i] = self.cpdf_post(mags,theta)  
        
            #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
            
        if sigma==1:        
            up = np.percentile(phi, 15.87, axis=0)       
            down = np.percentile(phi, 84.13, axis=0)       
        
        
        if sigma==3:
            up = np.percentile(phi, 0.135, axis=0)         
            down = np.percentile(phi, 99.865, axis=0)
           
        
        if plot_fig:     
            fig = plt.figure(figsize=(8, 6), dpi=100)
            ax = fig.add_subplot(1, 1, 1)
            ax.tick_params('both', which='major', length=7, width=1)
            ax.tick_params('both', which='minor', length=3, width=1)        
            ax.fill_between(mags, down, y2=up, color='orange', alpha=0.4) 
            ax.plot(mags, phi_fit, lw=1.5, c='red', zorder=3, label='Copula regress')        
            plt.errorbar(self.x, self.y, fmt=".k", capsize=0, lw=1.0,ms=2.5,label='data', alpha=0.5)
            plt.ylabel(r'$y$',fontsize=18)
            plt.xlabel(r'$x$',fontsize=18)
            plt.legend();
            #plt.xlim(lmin, self.Lmax)
            #plt.ylim(y1,y2)
            plt.show()
            
        result=np.array([mags,phi_fit,down,up])

        return result             

    # not used
    def regress(self, theta, xlim=None,ylim=None):  
        
        from tqdm import tqdm
        if self.data_loaded is False:
            temp = self.initialize() 
        
       
        
        lens=max(self.y)-min(self.y)
        self.y1 = min(self.y)-0.25*lens
        self.y2 = max(self.y)+0.25*lens        
        x1 = min(self.x) - 0.05* ( max(self.x)-min(self.x) ) 
        x2 = max(self.x) + 0.05* ( max(self.x)-min(self.x) )        
        mags=np.linspace(x1, x2,nmags)

        nsample = min(nsample,len(self.samples))        
        rsample = self.samples[np.random.randint(len(self.samples), size=nsample)]
        phi = np.zeros((nsample, nmags)) 
        
        
        #bf = np.median(self.samples, axis=0)
        if self.mcmc_fit_done is True:        
            bf = self.mcmc_fit                         # bf is best fit by MCMC
            #print('bestfit MCMC',bf)        
        else:
            print("The subroutine 'chain_analysis()' should be executed!") 

        phi_fit = self.cpdf_post(mags,bf)        
        
#        print('phi_fit')
#        print(phi_fit)
#        print(mags)
#        result=np.array([mags,phi_fit,phi_fit,phi_fit])
#        return result

        if progress_bar is True:            
            for i, theta in enumerate(tqdm(rsample)):                 
                phi[i] = self.cpdf_post(mags,theta) 
           
        else:
            for i, theta in enumerate(rsample): 
                phi[i] = self.cpdf_post(mags,theta)  
        
            #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
            
        if sigma==1:        
            up = np.percentile(phi, 15.87, axis=0)       
            down = np.percentile(phi, 84.13, axis=0)       
        
        
        if sigma==3:
            up = np.percentile(phi, 0.135, axis=0)         
            down = np.percentile(phi, 99.865, axis=0)
           
        
        if plot_fig:     
            fig = plt.figure(figsize=(8, 6), dpi=100)
            ax = fig.add_subplot(1, 1, 1)
            ax.tick_params('both', which='major', length=7, width=1)
            ax.tick_params('both', which='minor', length=3, width=1)        
            ax.fill_between(mags, down, y2=up, color='orange', alpha=0.4) 
            ax.plot(mags, phi_fit, lw=1.5, c='red', zorder=3, label='Copula regress')        
            plt.errorbar(self.x, self.y, fmt=".k", capsize=0, lw=1.0,ms=2.5,label='data')
            plt.ylabel(r'$y$',fontsize=18)
            plt.xlabel(r'$x$',fontsize=18)
            plt.legend();
            #plt.xlim(lmin, self.Lmax)
            #plt.ylim(y1,y2)
            plt.show()
            
        result=np.array([mags,phi_fit,down,up])

        return result 
























