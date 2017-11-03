import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { MDModule } from './modules/md.module';

import { AppComponent } from './app.component';
import { MainComponent } from './components/main/main.component';

@NgModule({
  declarations: [
    AppComponent,
    MainComponent
  ],
  imports: [
    BrowserModule,
    MDModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
