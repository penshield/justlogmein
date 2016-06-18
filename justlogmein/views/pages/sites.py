__author__ = 'snouto'

from system import *
from flask import render_template , request , session , flash , redirect , url_for
from controllers.PagesForms import UserSiteForm
from db.models import UserSite

@app.route('/account/sites/display',methods=['GET'])
@login_required
def sites_display():
    user = session['current_active_user']
    sites = UserSite.objects(user=user)
    return render_template('pages/sites.html',sites=sites)


@app.route('/account/sites/delete/<id>',methods=['GET'])
@login_required
def sites_delete(id):
    if id is None:
        return redirect(url_for('sites_display'))
    else:
        user = session['current_active_user']
        sites = UserSite.objects(user=user,id=id)
        if sites != None and len(sites) > 0:
            name = sites[0].name
            sites[0].delete()
            flash(u'%s has been Deleted Successfully' % name)

        return redirect(url_for('sites_display'))

@app.route('/account/sites/update/<id>',methods=['GET'])
@login_required
def sites_update(id):

    if id is None:
        return redirect(url_for('sites_display'))
    else:
        user = session['current_active_user']

        sites = UserSite.objects(user=user,id=id)
        form = UserSiteForm()
        form.load_site(sites[0])
        return render_template('pages/add-site.html',form=form)




@app.route('/account/sites/add',methods=['GET','POST'])
@login_required
def sites_add():

    form = UserSiteForm(request.form)
    if request.method =='GET':
        return render_template('pages/add-site.html',form=form)
    else:
        if form.validate_on_submit():
            site = form.get_site()
            user = session['current_active_user']
            site.user = user
            if site.icon == None or len(site.icon) <= 0:
                #site.icon = get_icon(site.url)
                if site.icon == None or len(site.icon) <= 0:
                    import base64
                    img = open('%s/img/na.png'%static_folder)
                    site.icon = base64.b64encode(img.read())

            site.save()
            flash(u'Site has been saved Successfully')
            return redirect(url_for('sites_display'))
        else:
            flash(u'Please Fill all the required fields below')
            return render_template('pages/add-site.html',form=form)



def get_icon(url):
    import  urllib2
    import base64
    import urlparse
    from cookielib import CookieJar
    from bs4 import BeautifulSoup
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    try:
        cj = CookieJar()
        req = urllib2.Request(url, headers=hdr)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        page = opener.open(req)
        soup = BeautifulSoup(page.read())
        icon_link = soup.find("link", rel="shortcut icon")
        if icon_link == None or icon_link['href'] == None:
            return None
        finalUrl = urlparse.urljoin(url,icon_link['href'])
        icon = urllib2.urlopen(finalUrl)
        if icon is not None:
            return base64.b64encode(icon.read())
        else:
            return None
    except Exception ,s:
        return None
