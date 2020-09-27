from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from datetime import datetime
import json


class MainView(View):
    def get(self, request, *args, **kwargs):
        return redirect('/news/')


class NewsCreate(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'news/create.html')

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        text = request.POST.get('text')

        with open(getattr(settings, 'NEWS_JSON_PATH'), 'r+', encoding='utf-8') as j:
            json_data = json.load(j)
            last_id = sorted([x['link'] for x in json_data])[-1]
            new_id = last_id + 1
            dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            new_post = {'created': dt, 'text': text,
                        'title': title, 'link': new_id}
            json_data.append(new_post)
            j.seek(0)
            j.write(json.dumps(json_data, ensure_ascii=False))
            j.truncate()

        return redirect('/news/')


class NewsView(View):
    def get(self, request, *args, **kwargs):
        json_data = None
        search_text = request.GET.get('q', None)
        with open(getattr(settings, 'NEWS_JSON_PATH'), 'r') as j:
            json_data = json.load(j)
        news_dict = dict()
        for new_temp in json_data:
            if search_text and search_text not in new_temp['title']:
                continue
            n = news_dict.get(new_temp['created'].split()[0], [])
            n.append(new_temp)
            news_dict[new_temp['created'].split()[0]] = n
        for key in news_dict.keys():
            ls = news_dict[key]
            news_dict[key] = sorted(ls, key=lambda k: k['created'],
                                    reverse=True)
        news_dict = dict(sorted(news_dict.items(), reverse=True))
        context = {'news': news_dict}
        return render(request, 'news/news.html', context=context)


class NewsDetail(View):
    def get(self, request, link_id, *args, **kwargs):
        json_data = None
        with open(getattr(settings, 'NEWS_JSON_PATH'), 'r') as j:
            json_data = json.load(j)
        for n in json_data:
            if n['link'] == link_id:
                context = {'title': n['title'], 'created': n['created'],
                           'text': n['text']}
                return render(request, 'news/new.html', context=context)