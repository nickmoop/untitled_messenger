import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { MatModule } from './modules/mat.module';

import { AppComponent } from './app.component';
import { MainComponent } from './components/main/main.component';
import { SvgIconComponent } from './components/svg-icon/svg-icon.component';

@NgModule({
  declarations: [
    AppComponent,
    MainComponent,
    SvgIconComponent
  ],
  imports: [
    BrowserModule,
    MatModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
