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
    import uuid
    if id is None:
        return redirect(url_for('sites_display'))
    else:
        user = session['current_active_user']

        sites = UserSite.objects(user=user,id=id)
        form = UserSiteForm()
        form.load_site(sites[0])
        return render_template('pages/add-site.html',form=form,uuid=uuid)




@app.route('/account/sites/add',methods=['GET','POST'])
@login_required
def sites_add():
    import uuid
    form = UserSiteForm(request.form)
    if request.method =='GET':
        return render_template('pages/add-site.html',form=form,uuid=uuid)
    else:
        site = form.get_site()
        field_names = request.form.getlist("field_name[]")
        field_values = request.form.getlist("field_value[]")
        field_types = request.form.getlist("field_type[]")
         #now let us zip them all
        fields_definition = zip(field_names,field_values,field_types)
        if fields_definition != None and len(fields_definition) > 0:
            for field_definition in fields_definition:
                    name , value , type = field_definition
                    site.fields.append({
                        'name':name,
                        'value':value,
                        'type':type
                    })
        if form.validate_on_submit():
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
            if site is not None:
                form.load_site(site)
            flash(u'Please Fill all the required fields below')
            return render_template('pages/add-site.html',form=form,uuid=uuid)



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
